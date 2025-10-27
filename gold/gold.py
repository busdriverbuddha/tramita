# # 1. Preparação
# 
# ## 1.1. Imports

import os

from pathlib import Path

import duckdb
import igraph as ig
import pandas as pd

from event import Event

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

# ## 1.2. Construção de nós e arestas
# 
# ### 1.2.1. Leitura do banco de dados
# 
# Aqui vamos consumir do banco de dados que construímos na fase silver, com alguns ajustes e correções para montar os grafos.

with duckdb.connect(DB_PATH, read_only=True) as con:

    house_props_df = con.execute("SELECT * FROM proposicoes_camara").df().set_index('id_proposicao', drop=True)
    house_autores_df = con.execute("SELECT * FROM autores_camara").df().set_index('id_autor', drop=True)
    house_deputados_df = con.execute("SELECT * FROM deputados_camara").df().set_index('id_deputado', drop=True)
    house_orgaos_df = con.execute("SELECT * FROM orgaos_camara").df().set_index('id_orgao', drop=True)
    house_partidos_df = con.execute("SELECT * FROM partidos_camara").df()
    house_partidos_membros_df = con.execute("SELECT * FROM partidos_membros_camara").df()

    senate_procs_df = con.execute("SELECT * FROM processo_senado").df().set_index('id_processo', drop=True)
    senate_autores_df = con.execute("SELECT * FROM autoria_iniciativa_senado").df().set_index('id_autoria_iniciativa', drop=True)
    senate_parlamentares_df = con.execute("SELECT * FROM parlamentar_senado").df().set_index('codigo_parlamentar', drop=True)
    senate_entes_df = con.execute("SELECT * FROM ente_senado").df().set_index('id_ente', drop=True)
    
    bill_match_df = con.execute("SELECT * FROM correspondencia_proposicoes_processo").df()

senate_parlamentares_df['tag'] = 'SS:' + senate_parlamentares_df.index.astype(str)


# ### 1.2.2. Filtragem 
# 
# Removemos da tabela de autorias as que não têm proposições ou processos listados

house_autores_df = house_autores_df[house_autores_df['id_proposicao'].isin(house_props_df.index)].copy()
senate_autores_df = senate_autores_df[senate_autores_df['id_processo'].isin(senate_procs_df.index)].copy()

# Da mesma forma, podemos eliminar deputados e órgãos e senadores não contemplados nas autorias

house_deputados_df = house_deputados_df[house_deputados_df.index.isin(
    house_autores_df[house_autores_df['tipo_autor'] == 'deputados']['id_deputado_ou_orgao'].unique()
)].copy()


house_orgaos_df = house_orgaos_df[house_orgaos_df.index.isin(
    house_autores_df[house_autores_df['tipo_autor'] == 'orgaos']['id_deputado_ou_orgao'].unique()
)].copy()

senate_parlamentares_df = senate_parlamentares_df[senate_parlamentares_df.index.isin(
    senate_autores_df['codigo_parlamentar'].unique()
)].copy()

# Alguns entes listados como autorias no Senado não têm registro no mesmo banco de dados.

missing_entes_df = senate_autores_df[
    senate_autores_df['sigla_ente'].isnull()
][['ente', 'sigla_tipo', 'descricao_tipo']].drop_duplicates()
missing_entes_df

# Alguns são apenas comissões da Câmara. Vamos substituir pelo ente da Câmara na base do Senado.

house_entes_in_senate = missing_entes_df[missing_entes_df['sigla_tipo'] == "COMISSAO_CAMARA"]
house_entes_in_senate

senate_entes_df.loc[2]

for index, row in senate_autores_df[senate_autores_df['sigla_tipo'] == "COMISSAO_CAMARA"].iterrows():
    senate_autores_df.at[index, 'ente'] = "Câmara dos Deputados"
    senate_autores_df.at[index, 'sigla_ente'] = "CD"
    senate_autores_df.at[index, 'sigla_tipo'] = "CASA_LEGISLATIVA"

# Vamos criar pseudo-entradas para outros entes relevantes.

nomes_e_siglas = {
    'Superior Tribunal de Justiça': '_STJ', 
    'Procuradoria-Geral da República': '_PGR',
    'Ministério Público da União': '_MPU',
    'Defensoria Pública da União': '_DPU',
}
# para cada uma das autorias faltantes, vamos criar novas linhas em senate_entes_df
# preservando id_ente como índice
k = 0
new_rows = []
new_index = []
for idx, row in missing_entes_df.iterrows():
    sigla = nomes_e_siglas.get(row['ente'])
    new_id = 9999990 + k
    new_row = {
        'sigla': sigla,
        'nome': row['ente'],
        'casa': None,
        'sigla_tipo': row['sigla_tipo'],
        'descricao_tipo': row['descricao_tipo'],
        'data_inicio': None,
        'data_fim': None,
        'tag': f'SE:{new_id}'
    }
    new_rows.append(new_row)
    new_index.append(new_id)
    k += 1

if new_rows:
    new_df = pd.DataFrame(new_rows, index=new_index)
    # manter o nome do índice (esperado: 'id_ente')
    new_df.index.name = senate_entes_df.index.name
    # concatenar preservando os índices
    senate_entes_df = pd.concat([senate_entes_df, new_df], axis=0)

# Como a tabela de autorias do Senado lista os entes por sigla e não por id, agora preenchemos isso naquela.

for index, row in missing_entes_df.iterrows():
    sigla = nomes_e_siglas.get(row['ente'])
    senate_autores_df.loc[
        (senate_autores_df['ente'] == row['ente']) &
        (senate_autores_df['sigla_ente'].isnull()),
        'sigla_ente'
    ] = sigla

# Agora fazemos o caminho inverso. Mantemos em senate_entes_df somente o que aparece em senate_autores_df. Ou seja, somente onde senate_entes_df.sigla está em senate_autores_df.sigla_ente


senate_entes_df = senate_entes_df[senate_entes_df['sigla'].isin(
    senate_autores_df['sigla_ente'].unique()
)]

# Se houver duplicadas em sigla_ente, mantemos a primeira ocorrência
senate_entes_df = senate_entes_df.drop_duplicates(subset=['sigla'], keep='first')

# Finalmente, criamos a coluna id_ente em senate_autores_df a partir de sigla_ente usando senate_entes_lookup_df

senate_entes_lookup_df = senate_entes_df[['sigla']].copy()
senate_entes_lookup_df['id_ente'] = senate_entes_lookup_df.index
senate_entes_lookup_df.set_index('sigla', drop=True, inplace=True)
senate_entes_lookup_df

senate_autores_df['id_ente'] = senate_autores_df['sigla_ente'].map(senate_entes_lookup_df['id_ente'])

# ### 1.2.3. Consolidação de órgaos e entes
# 
# Tentamos fazer uma correspondência entre os órgãos da Câmara e os entes do Senado

entity_match_df = pd.DataFrame([
    {"id_ente": 2, "id_orgao": 100292},  # Câmara
    {"id_ente": 1, "id_orgao": 78},  # Senado
    {"id_ente": 55126, "id_orgao": 60},  # Presidência
    {"id_ente": 55126, "id_orgao": 253},  # Poder Executivo - depois vamos consolidar com presidência
    {"id_ente": 5282726, "id_orgao": 80},  # STF
    {"id_ente": 9999990, "id_orgao": 81},  # STJ
    {"id_ente": 7351348, "id_orgao": 277},  # TSE
    {"id_ente": 7352253, "id_orgao": 82},  # TCU
    {"id_ente": 55143, "id_orgao": 382},  # TJDFT
    {"id_ente": 9999991, "id_orgao": 101347},  # PGR
    {"id_ente": 9999992, "id_orgao": 57},  # MPU
    {"id_ente": 9999994, "id_orgao": 101131},  # DPU
])
entity_match_df

# Verificamos.

entity_match_df.join(house_orgaos_df['nome'], on="id_orgao").join(senate_entes_df['nome'], on="id_ente", lsuffix="_camara", rsuffix="_senado")

# Normalizamos.

entity_match_df['ente_tag'] = "SE:" + entity_match_df['id_ente'].astype(str)
entity_match_df['orgao_tag'] = "CO:" + entity_match_df['id_orgao'].astype(str)
entity_match_df = entity_match_df.join(house_orgaos_df['nome'], on="id_orgao")
entity_match_df = entity_match_df.drop(['id_ente', 'id_orgao'], axis=1)
entity_match_df

# ### 1.2.4. Extração do partido dos parlamentares
# 
# Enquanto no Senado, o partido e a UF já vêm junto com os detalhes de cada parlamentar, na Câmara essa informação deve ser buscada indiretamente. Por algum motivo não conseguimos a totalidade das informações na fase Bronze e Prata, então fazemos agora.

house_deputados_df.join(house_partidos_membros_df.drop_duplicates('id_deputado', keep='last').set_index('id_deputado', drop=True)[['id_partido']], on="id_deputado")

# Este foi o código usado para baixar as informações:

# Não temos dados suficientes. Temos que buscar na API

# import httpx
# import asyncio
# import re

# response = httpx.get("https://dadosabertos.camara.leg.br/api/v2/partidos/", params={'dataInicio': '2019-01-01', 'dataFim': '2025-01-01', 'itens': '100'})
# data = response.json()

# pids = [d['id'] for d in data['dados']]


# pat = re.compile(r"&pagina=(\d+)&")

# async def get_membros(sem, client, id_partido):
#     async with sem:
#         all_data = []
#         print(id_partido)
#         for retry in range(10):
#             try:
#                 response = await client.get(
#                     f"https://dadosabertos.camara.leg.br/api/v2/partidos/{id_partido}/membros",
#                     params={'dataInicio': '2019-01-01', 'dataFim': '2025-01-01', 'itens': '15'}
#                 )
#                 response.raise_for_status()
#                 data = response.json()
#                 all_data.extend(data['dados'])
#                 for link in data.get('links', []):
#                     if link.get('rel', '') == 'last':
#                         n_pages = int(pat.findall(link['href'])[0])
#                         break
#                 else:
#                     return all_data
#                 for page in range(2, n_pages + 1):
#                     response = await client.get(
#                         f"https://dadosabertos.camara.leg.br/api/v2/partidos/{id_partido}/membros",
#                         params={'dataInicio': '2019-01-01', 'dataFim': '2025-01-01', 'itens': '15', 'pagina': page}
#                     )
#                     response.raise_for_status()
#                     data = response.json()
#                     all_data.extend(data['dados'])
#                 return all_data
#             except Exception as e:
#                 print(e)
#                 print(f"Retrying {id_partido}...")
#                 await asyncio.sleep(4)
    
# sem = asyncio.Semaphore(4)
# async with httpx.AsyncClient() as client:
#     tasks = [get_membros(sem, client, ip) for ip in pids]
#     result = await asyncio.gather(*tasks)
# partido_rows = []
# for r in result:
#     partido_rows.extend(r)
    
# partido_df = pd.DataFrame(partido_rows)
# partido_df = partido_df.sort_values('idLegislatura').drop_duplicates('id', keep='last').copy()
# partido_df['partido'] = partido_df['siglaPartido'] + "/" + partido_df['siglaUf']
# partido_df.to_pickle("partidos_membros_camara.pkl")

partido_df = pd.read_pickle("partidos_membros_camara.pkl")

house_deputados_df = house_deputados_df.join(partido_df.set_index('id', drop=True)[['partido']], on="id_deputado")

# Mesmo assim, vemos que alguns ficaram faltando.

house_deputados_df.value_counts('partido', dropna=False)

senate_parlamentares_df['partido'] = senate_parlamentares_df['sigla_partido'] + "/" + senate_parlamentares_df['uf_parlamentar']

# ### 1.2.5. Execução da construção.
# 
# Agora que temos os dados necessários, criamos e registramos os nós e arestas.
# 
# **Nós:**

nodes_df = pd.concat([
    house_props_df[["prop_tag", "prop_label"]].rename(columns={"prop_tag": "tag", "prop_label": "label"}),
    house_deputados_df[["tag", "nome_civil", "partido"]].rename(columns={"nome_civil": "label"}),
    house_orgaos_df[["tag", "nome"]].rename(columns={"nome": "label"}),
    senate_procs_df[["tag", "identificacao"]].rename(columns={"identificacao": "label"}),
    senate_parlamentares_df[["tag", "nome_parlamentar", "partido"]].rename(columns={"nome_parlamentar": "label"}),
    senate_entes_df[["tag", "nome"]].rename(columns={"nome": "label"}),
], ignore_index=True).drop_duplicates().reset_index(drop=True)

def get_node_type(tag: str) -> str:
    prefix = tag[:3]
    match prefix:
        case 'CP:':
            return 'Proposicao'
        case 'CD:':
            return 'Deputado'
        case 'CO:':
            return 'Orgao'
        case 'SP:':
            return 'Processo'
        case 'SS:':
            return 'Senador'
        case 'SE:':
            return 'Ente'
        case _:
            return 'Unknown'
    
nodes_df['type'] = nodes_df['tag'].apply(get_node_type)


# **Arestas:**

def get_senate_auth_tag(row):
    if row['sigla_ente'] == 'SF' and not pd.isna(row['codigo_parlamentar']):
        return f"SS:{row['codigo_parlamentar']}"
    else:
        return f"SE:{row['id_ente']}"
        
senate_autores_df['proc_tag'] = senate_autores_df['id_processo'].apply(lambda x: f"SP:{x}")
senate_autores_df['auth_tag'] = senate_autores_df.apply(get_senate_auth_tag, axis=1)


house_edges_df = house_autores_df[house_autores_df['proponente']].copy()
house_edges_df['prop_label'] = 'CP:' + house_edges_df['id_proposicao'].astype(str)
house_edges_df['auth_label'] = house_edges_df.apply(
    lambda row: f"CD:{row['id_deputado_ou_orgao']}" if row['tipo_autor'] == 'deputados' else f"CO:{row['id_deputado_ou_orgao']}",
    axis=1
)
house_edges_df = house_edges_df[['auth_label', 'prop_label']].rename(columns={'auth_label': 'source', 'prop_label': 'target'})

senate_edges_df = senate_autores_df.copy()
senate_edges_df.rename(columns={'auth_tag': 'source', 'proc_tag': 'target'}, inplace=True)
senate_edges_df = senate_edges_df[['source', 'target']]
senate_edges_df

edges_df = pd.concat([house_edges_df, senate_edges_df], ignore_index=True)
edges_df['etype'] = 'autoria'
edges_df

nodes_df

# Criamos também arestas de correspondência entre projetos de lei da Câmara e do Senado

bill_match_df['house_tag'] = 'CP:' + bill_match_df['id_proposicao_camara'].astype(str)
bill_match_df['senate_tag'] = 'SP:' + bill_match_df['id_processo_senado'].astype(str)
bill_match_df


common_labels = set(nodes_df[nodes_df['type'] == 'Proposicao']['label']).intersection(set(nodes_df[nodes_df['type'] == 'Processo']['label']))
filtered_bill_match_df = bill_match_df[bill_match_df['identificacao'].isin(common_labels)]
filtered_bill_match_df

filtered_bill_match_df = filtered_bill_match_df[['house_tag', 'senate_tag']].rename(columns={'house_tag': 'source', 'senate_tag': 'target'})
filtered_bill_match_df['etype'] = 'correspondencia'
filtered_bill_match_df

# Acrescentamos um caso especial, das duas fases da PEC 10/2020

filtered_bill_match_df = pd.concat([
    filtered_bill_match_df,
    pd.DataFrame([{'source': 'CP:2242583', 'target': 'CP:2249946', 'etype': 'correspondencia'}])
])

# Agora fazemos o mesmo para órgãos (Câmara) e entes (Senado)

entity_match_df = entity_match_df[['orgao_tag', 'ente_tag']].rename(columns={'orgao_tag': 'source', 'ente_tag': 'target'})
# adicionamos a correspondência entre presidente da república e poder executivo na câmara
entity_match_df = pd.concat([entity_match_df, pd.DataFrame([{'source': 'CO:60', 'target': 'CO:253'}])])
entity_match_df['etype'] = 'correspondencia'


edges_df = pd.concat([edges_df, filtered_bill_match_df, entity_match_df], ignore_index=True)

edges_df.to_parquet(EDGES_PATH_PARQUET, index=False)
edges_df.to_csv(EDGES_PATH_CSV, index=False)

# fazemos uma última checagem para descobrir vértices órfãos

nodes_df = nodes_df[nodes_df['tag'].isin(edges_df['source']) | nodes_df['tag'].isin(edges_df['target'])]


nodes_df.to_parquet(NODES_PATH_PARQUET, index=False)
nodes_df.to_csv(NODES_PATH_CSV, index=False)

nodes_df.shape, edges_df.shape