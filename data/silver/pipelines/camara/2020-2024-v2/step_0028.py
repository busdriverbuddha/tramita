# ### 2.2.5 Votos
import tempfile
from glob import glob
import json
import pandas as pd
import pyarrow.parquet as pq

with tempfile.NamedTemporaryFile() as tf:
    paths = glob("data/bronze/snapshots/bronze-2020-2024-v2/camara/votos/year=*/part-*.parquet")
    table = pq.read_table(paths)
    df = table.to_pandas()

    exploded_rows = []
    for _, row in df.iterrows():
        payload = json.loads(row["payload_json"])
        for item in payload["dados"]:
            exploded_rows.append({
                "id_votacao": row["id"],
                "id_deputado": item["deputado_"]["id"],
                "tipo_voto": item["tipoVoto"],
                "data_hora": item["dataRegistroVoto"],
                "year_snapshot": row["year"],
            })

    exploded_df = pd.DataFrame(exploded_rows)
    exploded_df.to_csv(tf.name, index=False)

    conn.execute("""
        DROP TABLE IF EXISTS votos_camara;

        -- Create table with PK declared up-front
        CREATE TABLE votos_camara (
            id_voto BIGINT PRIMARY KEY,
            id_votacao TEXT,
            id_deputado BIGINT,
            tipo_voto TEXT,
            data_hora TIMESTAMP,
            year_snapshot INTEGER
        );

        -- Deterministic incremental ID via ROW_NUMBER with ORDER BY
        INSERT INTO votos_camara
        SELECT
            ROW_NUMBER() OVER (ORDER BY id_votacao, id_deputado, data_hora, year_snapshot) AS id_voto,
            CAST(id_votacao AS TEXT)                           AS id_votacao,
            CAST(id_deputado AS BIGINT)                        AS id_deputado,
            CAST(tipo_voto AS TEXT)                            AS tipo_voto,
            CAST(data_hora AS TIMESTAMP)                       AS data_hora,
            CAST(year_snapshot AS INTEGER)                     AS year_snapshot
        FROM read_csv_auto($path, HEADER=TRUE);
    """, {"path": tf.name})
