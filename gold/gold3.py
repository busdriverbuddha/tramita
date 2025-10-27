# # 3. Qualificação de vértices de acordo com tramitação no Congresso
# 
# ## 3.1. Preparação
# 
# ## 3.1.1. Imports

import os

from pathlib import Path

import duckdb
import igraph as ig
import pandas as pd

from event import Event  # Enum customizado nosso para eventos relevantes de tramitação

from dotenv import load_dotenv

load_dotenv()

PROJECT_DIR = Path("~/tramita").expanduser()
DB_PATH = PROJECT_DIR / os.getenv("SILVER_DUCKDB_PATH", "")
OUT_DIR = PROJECT_DIR / "data" / "gold"
OUT_DIR.mkdir(exist_ok=True)

NODES_PATH_PARQUET = OUT_DIR / "nodes.parquet"
EDGES_PATH_PARQUET = OUT_DIR / "edges.parquet"
NODES_PATH_CSV = OUT_DIR / "nodes.csv"
EDGES_PATH_CSV = OUT_DIR / "edges.csv"

# ## 3.1.2. Leitura do banco de dados

with duckdb.connect(DB_PATH, read_only=True) as con:
    house_props_df = con.execute("SELECT * FROM proposicoes_camara").df().set_index('id_proposicao', drop=True)
    house_tram_df = con.execute("SELECT * FROM tramitacoes_camara").df()
    house_autores_df = con.execute("SELECT * FROM autores_camara").df().set_index('id_autor', drop=True)
    house_deputados_df = con.execute("SELECT * FROM deputados_camara").df().set_index('id_deputado', drop=True)
    house_orgaos_df = con.execute("SELECT * FROM orgaos_camara").df().set_index('id_orgao', drop=True)
    senate_procs_df = con.execute("SELECT * FROM processo_senado").df().set_index('id_processo', drop=True)
house_tram_df = house_tram_df[house_tram_df['id_proposicao'].isin(house_props_df.index)].copy().set_index('id_tramitacao', drop=True)
house_tram_df

# ## 3.2. Construção da tabela de tramitações
# 
# A partir daqui vamos executar uma série de passos para cosntruir uma tabela completa com as tramitações de cada proposição em cada casa

# ### 3.2.1. Câmara dos Deputados

house_tram_expanded_df = house_tram_df.join(house_props_df, on="id_proposicao", how="left", lsuffix="tram", rsuffix="props")[[
    'id_proposicao',
    'prop_label',
    'sequencia',
    'data_hora',
    'descricao_tramitacao',
    'sigla_orgao',
    'despacho',
    'cod_situacao',
    'descricao_situacao',
    'regime',
    'apreciacao',
    'cod_tipo_tramitacao',
    'uri_orgao',
    # 'prop_tag',
]].sort_values(['id_proposicao', 'data_hora'])
house_tram_expanded_df

# Não tínhamos todos os dados dos órgãos da Câmara, então baixamos da API.

# import asyncio
# import httpx
# orgaos_df = house_tram_expanded_df[['sigla_orgao', 'uri_orgao']].drop_duplicates()
# async def get_data(uri: str, client: httpx.AsyncClient, sem: asyncio.Semaphore):
#     async with sem:
#         print(uri)
#         response = await client.get(uri)
#         response.raise_for_status()
#         return response.json()

# sem = asyncio.Semaphore(4)
# async with httpx.AsyncClient() as client:
#     tasks = [get_data(uri, client, sem) for uri in orgaos_df['uri_orgao']]
#     result = await asyncio.gather(*tasks)
# rows = [r['dados'] for r in result]
# full_orgaos_df = pd.DataFrame(rows).set_index('uri', drop=True)
# full_orgaos_df.to_pickle('full_orgaos_camara_df.pkl')


full_orgaos_df = pd.read_pickle('full_orgaos_camara_df.pkl')

house_tram_expanded_df = house_tram_expanded_df.join(
    full_orgaos_df[['nome', 'codTipoOrgao', 'tipoOrgao']],
    on="uri_orgao",
    how="left",
).rename(columns={'codTipoOrgao': 'cod_tipo_orgao', 'tipoOrgao': 'tipo_orgao', 'nome': 'nome_orgao'}).copy()
house_tram_expanded_df['data_hora'] = pd.to_datetime(house_tram_expanded_df['data_hora'])
house_tram_expanded_df

# Excluímos alguns órgãos que não são relevantes ou corretos.

orgao_code_excludes = [
    70_000,  # Sociedade Civil (provavelmente erro)
    12_000,  # Órgãos burocráticos da Câmara (só protocolar)
    40_000,  # Senado Federal; veremos lá e não cá
    10,      # Grupos de trabalho, nada relevante
    11,      # Conselho de Ética da Câmara; irrelevante
]

house_tram_expanded_filtered_df = house_tram_expanded_df[
    (~house_tram_expanded_df['cod_tipo_orgao'].isin(orgao_code_excludes))
].sort_values(['id_proposicao', 'sequencia'])
house_tram_expanded_filtered_df

# A função abaixo extrai um `Event`, onde possível, para cada fileira da tabela de tramitações da Câmara

def house_row_to_event(row: pd.Series) -> Event | None:
    # apresentado
    if row['cod_tipo_tramitacao'] == '100':
        return Event.APRESENTADO

    # distribuído
    if row['cod_tipo_tramitacao'] == '110':
        return Event.DISTRIBUIDO

    # recebido em comissão
    if row['cod_tipo_tramitacao'] == '500' and row['tipo_orgao'].startswith('Comissão'):
        return Event.RECEBIDO_COMISSAO

    # designado relator em comissão
    if row['cod_tipo_tramitacao'] == '320' and row['tipo_orgao'].startswith('Comissão'):
        return Event.DESIGNADO_RELATOR_COMISSAO

    # retirado de pauta em comissão
    if row['cod_tipo_tramitacao'] == '250' and row['tipo_orgao'].startswith('Comissão'):
        return Event.RETIRADO_PAUTA_COMISSAO

    # aprovada urgência
    if row['cod_tipo_tramitacao'] == '196':
        return Event.APROVADA_URGENCIA

    # designado relator em plenário
    if row['cod_tipo_tramitacao'] == '320' and row['sigla_orgao'] == 'PLEN':
        return Event.DESIGNADO_RELATOR_PLENARIO

    # remetido
    if row['cod_tipo_tramitacao'] == '128':
        return Event.REMETIDO_AO_SENADO
    if row['cod_tipo_tramitacao'] == '609':
        return Event.REMETIDO_A_SANCAO
    if row['cod_tipo_tramitacao'] == '608':
        return Event.REMETIDO_A_PROMULGACAO
    if row['cod_tipo_tramitacao'] == '100' and row['despacho'].startswith('Remessa ao Senado Federal'):
        return Event.REMETIDO_AO_SENADO
    if row['cod_tipo_tramitacao'] == '1243' and row['despacho'].startswith('A matéria vai à sanção'):
        return Event.REMETIDO_A_SANCAO

    # aprovado em plenário
    if row['cod_tipo_tramitacao'] == '1235':
        return Event.APROVADO_PLENARIO

    # rejeitado em plenário
    # Não tem como saber ao certo
    pass

    # arquivado
    if row['cod_tipo_tramitacao'] in ['502', '1024']:
        return Event.ARQUIVADO

    # desarquivado
    if row['cod_tipo_tramitacao'] == '503':
        return Event.DESARQUIVADO

# Consolidamos a tabela de eventos para a Câmara

df_with_events = house_tram_expanded_filtered_df.copy()
df_with_events['event'] = df_with_events.apply(house_row_to_event, axis=1)
df_with_events = df_with_events[df_with_events['event'].notnull()]


house_event_df = (df_with_events[['id_proposicao', 'prop_label', 'data_hora', 'event', 'sigla_orgao']]
    .sort_values(['data_hora', 'id_proposicao'])
    .reset_index(drop=True)
    .rename(columns={
        'data_hora': 'event_ts',
        'sigla_orgao': 'event_loc',
    }))


# ### 3.2.2. Senado Federal

with duckdb.connect(DB_PATH, read_only=True) as con:
    senate_desp_df = con.execute("SELECT * FROM despachos_senado").df().set_index('id_despacho', drop=True)
    senate_prov_df = con.execute("SELECT * FROM providencias_senado").df().set_index('id_providencia', drop=True)
    senate_sit_df = con.execute("SELECT * FROM situacoes_senado").df().set_index('id_situacao', drop=True)
    senate_aut_df = con.execute("SELECT * FROM autuacoes_senado").df()
    senate_inf_df = con.execute("SELECT * FROM informes_legislativos_senado").df().set_index('id_informe_legislativo', drop=True)
    senate_unid_df = con.execute("SELECT * FROM unidades_destinatarias_senado").df().set_index('id_unidade_destinataria', drop=True)
    
def filter_by_processo(df):
    return df[df['id_processo'].isin(senate_procs_df.index)]

senate_desp_df = filter_by_processo(senate_desp_df)
senate_prov_df = filter_by_processo(senate_prov_df)
senate_sit_df = filter_by_processo(senate_sit_df)
senate_aut_df = filter_by_processo(senate_aut_df)
senate_inf_df = filter_by_processo(senate_inf_df)
senate_unid_df = filter_by_processo(senate_unid_df)

senate_event_rows = []
for id_processo, row in senate_procs_df.iterrows():
    if not pd.isna(row['documento_data_apresentacao']):
        senate_event_rows.append(
            {
                'id_processo': id_processo,
                'proc_label': row['identificacao'],
                'event_ts': row['documento_data_apresentacao'],
                'event': Event.APRESENTADO,
                'event_loc': "SF",
            }
        )
        

# Extraímos dos Informes Legislativos as designações de relator em comissão

senate_dist_df_ = senate_inf_df[senate_inf_df['descricao'].str.match(r"^(re)?distribuído", case=False)]
senate_dist_df_ = senate_dist_df_[senate_dist_df_['id_processo'].isin(senate_procs_df.index)]

for index, row in senate_dist_df_.iterrows():
    senate_event_rows.append({
        'id_processo': row['id_processo'],
        'proc_label': senate_procs_df.loc[row['id_processo'], 'identificacao'],
        'event_ts': row['data_informe'],
        'event': Event.DESIGNADO_RELATOR_COMISSAO,
        'event_loc': row['colegiado_sigla'],
    })

# E das unidades de destino, a recepção em Comissão

senate_unid_ext_df = senate_unid_df.join(senate_desp_df, on="id_despacho", lsuffix="_unid", rsuffix="_desp")\
    .join(senate_prov_df, on="id_providencia", lsuffix="_unid", rsuffix="_prov")\
        .join(senate_procs_df[['identificacao']], on="id_processo")

# distribuído / recebido em comissão (dá na mesma aqui)
for index, row in senate_unid_ext_df.iterrows():
    senate_event_rows.append({
        'id_processo': row['id_processo_unid'],
        'proc_label': row['identificacao'],
        'event_ts': row['data_despacho'],
        'event': Event.RECEBIDO_COMISSAO,
        'event_loc': row['colegiado_sigla'],
    })

# Da mesma forma, extraímos as aprovações de urgência, retiradas de pauta, designações de relator em plenário

def aprov_urgencia(descricao):
    for line in descricao.splitlines():
        line = line.lower()
        if "aprovado" in line and "urgência" in line:
            if line.index("aprovado") < line.index("urgência"):
                return True
    return False

# aprovada urgência
for index, row in senate_inf_df[senate_inf_df['descricao'].apply(aprov_urgencia)].iterrows():
    id_proc = row['id_processo']
    proc_label = senate_procs_df.loc[id_proc, 'identificacao']
    senate_event_rows.append({
        'id_processo': id_proc,
        'proc_label': proc_label,
        'event_ts': row['data_informe'],
        'event': Event.APROVADA_URGENCIA,
        'event_loc': row['colegiado_sigla'],
    })

def retirada_pauta(descricao):
    for line in descricao.splitlines():
        line = line.lower()
        if "a matéria foi retirada de pauta" in line or "a matéria é retirada de pauta" in line:
            return True
    return False

# retirada de pauta em comissão
for index, row in senate_inf_df[senate_inf_df['descricao'].apply(retirada_pauta)].iterrows():
    if row['colegiado_sigla'] == "PLEN":
        continue
    id_proc = row['id_processo']
    proc_label = senate_procs_df.loc[id_proc, 'identificacao']
    senate_event_rows.append({
        'id_processo': id_proc,
        'proc_label': proc_label,
        'event_ts': row['data_informe'],
        'event': Event.RETIRADO_PAUTA_COMISSAO,
        'event_loc': row['colegiado_sigla'],
    })

def relator_plenario(row):
    if row['colegiado_sigla'] != "PLEN":
        return False
    desc = row['descricao'].lower()
    return desc.startswith("designad") and "relator" in desc

for _, row in senate_inf_df[senate_inf_df.apply(relator_plenario, axis=1)].iterrows():
    id_proc = row['id_processo']
    proc_label = senate_procs_df.loc[id_proc, 'identificacao']
    senate_event_rows.append({
        'id_processo': id_proc,
        'proc_label': proc_label,
        'event_ts': row['data_informe'],
        'event': Event.DESIGNADO_RELATOR_PLENARIO,
        'event_loc': row['colegiado_sigla'],
    })

# E finalmente as situações iniciadas conforme indicado nos informes legislativos

# demais situaçòes iniciadas
for _, row in senate_inf_df.iterrows():
    id_proc = row['id_processo']
    proc_label = senate_procs_df.loc[id_proc, 'identificacao']
    event_type = None
    sig = row['sigla_situacao_iniciada']
    if sig is None:
        continue
    if sig.startswith("APRVD"):
        event_type = Event.APROVADO_PLENARIO
    if sig == "ARQVD":
        event_type = Event.ARQUIVADO
    if sig == "RTPA":
        event_type = Event.RETIRADO_PAUTA_COMISSAO
    if sig == "RMSAN":
        event_type = Event.REMETIDO_A_SANCAO
    if sig == "RMCD":
        event_type = Event.REMETIDO_A_CAMARA
    if sig == "RMPRO":
        event_type = Event.REMETIDO_A_PROMULGACAO
    if sig.startswith("RJTDA"):
        event_type = Event.REJEITADO_PLENARIO
        
    if event_type is not None:
        senate_event_rows.append({
            'id_processo': id_proc,
            'proc_label': proc_label,
            'event_ts': row['data_informe'],
            'event': event_type,
            'event_loc': "PLEN",  # sometimes is None but all of this is plenário-related
        })

# Construímos a tabela de eventos do Senado

senate_event_df = pd.DataFrame(senate_event_rows).sort_values(['event_ts', 'id_processo']).reset_index(drop=True)
senate_event_df

# ### 3.2.3. Tabela conjunta

senate_event_df['casa'] = "senado"
house_event_df['casa'] = "camara"

full_event_df = pd.concat([
    house_event_df.drop('id_proposicao', axis=1).rename(columns={'prop_label': 'label'}),
    senate_event_df.drop('id_processo', axis=1).rename(columns={'proc_label': 'label'})
], ignore_index=True).sort_values(['label', 'event_ts']).reset_index(drop=True)
full_event_df

full_event_df = full_event_df[full_event_df[['label', 'event', 'casa']].ne(
    full_event_df[['label', 'event', 'casa']].shift()
).any(axis=1)].reset_index(drop=True)
full_event_df

full_event_df = full_event_df.join(
    house_props_df.set_index('prop_label')['prop_tag'],
    on="label"
).join(
    senate_procs_df.set_index('identificacao')[['tag']].rename(columns={'tag': 'proc_tag'}),
    on="label",
)

full_event_df.to_pickle('full_event_df.pkl')