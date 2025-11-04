# # 3. Senado Federal
# ## Entes
# ### Puxamos a lista completa de entes
import httpx
import pandas as pd


def get_entes():
    with httpx.Client() as client:
        response = client.get("https://legis.senado.leg.br/dadosabertos/processo/entes")
        response.raise_for_status()
        data = response.json()
        return data

data = get_entes()
entes_df = pd.DataFrame(data)
entes_df.columns = ['id_ente', 'sigla', 'nome', 'casa', 'sigla_tipo', 'descricao_tipo', 'data_inicio', 'data_fim']

conn.execute("""CREATE OR REPLACE TABLE ente_senado (
    id_ente BIGINT PRIMARY KEY,
    sigla VARCHAR,
    nome VARCHAR,
    casa VARCHAR,
    sigla_tipo VARCHAR,
    descricao_tipo VARCHAR,
    data_inicio DATE,
    data_fim DATE
);""")

conn.register("ente_df", entes_df)
conn.execute("INSERT INTO ente_senado SELECT * FROM ente_df")

conn.execute("""ALTER TABLE ente_senado ADD COLUMN IF NOT EXISTS tag VARCHAR;
UPDATE ente_senado SET tag = 'SE:' || CAST(id_ente AS VARCHAR);""")

conn.unregister('ente_df')