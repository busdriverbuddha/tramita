# ### 2.3.7 Legislaturas e líderes

import tempfile
from glob import glob
import pyarrow.parquet as pq
import json
import pandas as pd


with tempfile.NamedTemporaryFile() as tf:
    paths = glob("data/bronze/snapshots/bronze-2020-2024-v2/camara/legislaturas/lideres/year=*/part-*.parquet")
    table = pq.read_table(paths)
    df = table.to_pandas()

    exploded_rows = []
    for _, row in df.iterrows():
        payload = json.loads(row["payload_json"])
        for item in payload["dados"]:
            exploded_rows.append({
                "id_legislatura": row["id"],
                "nome_bancada": item["bancada"]["nome"],
                "tipo_bancada": item["bancada"]["tipo"],
                "uri_bancada": item["bancada"]["uri"],
                "data_inicio": item["dataInicio"],
                "data_fim": item["dataFim"],
                "id_deputado": item["parlamentar"]["id"],
                "titulo": item["titulo"],
                "year_snapshot": row["year"],
            })

    exploded_df = pd.DataFrame(exploded_rows)
    exploded_df.to_csv(tf.name, index=False)

    conn.execute("""
        DROP TABLE IF EXISTS legislaturas_lideres_camara;

        -- Create with surrogate PK
        CREATE TABLE legislaturas_lideres_camara (
            id_lider BIGINT PRIMARY KEY,
            id_legislatura BIGINT,
            nome_bancada TEXT,
            tipo_bancada TEXT,
            uri_bancada TEXT,
            data_inicio TIMESTAMP,
            data_fim TIMESTAMP,
            id_deputado BIGINT,
            titulo TEXT,
            year_snapshot INTEGER
        );

        -- Insert with deterministic incremental ID
        INSERT INTO legislaturas_lideres_camara
        SELECT
            ROW_NUMBER() OVER (
                ORDER BY
                    CAST(id_legislatura AS BIGINT),
                    COALESCE(nome_bancada, ''),
                    COALESCE(tipo_bancada, ''),
                    COALESCE(id_deputado, -1),
                    CAST(year_snapshot AS INTEGER)
            ) AS id_lider,
            CAST(id_legislatura AS BIGINT)         AS id_legislatura,
            CAST(nome_bancada AS TEXT)             AS nome_bancada,
            CAST(tipo_bancada AS TEXT)             AS tipo_bancada,
            CAST(uri_bancada AS TEXT)              AS uri_bancada,
            CAST(data_inicio AS TIMESTAMP)         AS data_inicio,
            CAST(data_fim AS TIMESTAMP)            AS data_fim,
            CAST(id_deputado AS BIGINT)            AS id_deputado,
            CAST(titulo AS TEXT)                   AS titulo,
            CAST(year_snapshot AS INTEGER)         AS year_snapshot
        FROM read_csv_auto($path, HEADER=TRUE);
    """, {"path": tf.name})
