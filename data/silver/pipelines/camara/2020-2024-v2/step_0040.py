import tempfile
from glob import glob
import pyarrow.parquet as pq
import json
import pandas as pd

with tempfile.NamedTemporaryFile() as tf:
    paths = glob("data/bronze/snapshots/bronze-2020-2024-v2/camara/eventos/pauta/year=*/part-*.parquet")
    table = pq.read_table(paths)
    df = table.to_pandas()

    exploded_rows = []
    for _, row in df.iterrows():
        payload = json.loads(row["payload_json"])
        for item in payload["dados"]:
            exploded_rows.append({
                "id_evento": row["id"],
                "cod_regime": item.get("codRegime"),
                "ordem": item.get("ordem"),
                "id_proposicao": (item.get("proposicao_", {}) or {}).get("id"),
                "id_relator": (item.get("relator") or {}).get("id") if item.get("relator") else None,
                "year_snapshot": row["year"],
            })

    exploded_df = pd.DataFrame(exploded_rows)
    exploded_df.to_csv(tf.name, index=False)

    conn.execute("""
        DROP TABLE IF EXISTS eventos_pauta_camara;

        -- Create table with surrogate PK
        CREATE TABLE eventos_pauta_camara (
            id_pauta BIGINT PRIMARY KEY,
            id_evento BIGINT,
            cod_regime TEXT,
            ordem INTEGER,
            id_proposicao BIGINT,
            id_relator BIGINT,
            year_snapshot INTEGER
        );

        -- Deterministic incremental ID via ROW_NUMBER
        INSERT INTO eventos_pauta_camara
        SELECT
            ROW_NUMBER() OVER (
                ORDER BY
                    CAST(id_evento AS BIGINT),
                    CAST(ordem AS INTEGER),
                    CAST(id_proposicao AS BIGINT),
                    COALESCE(TRY_CAST(id_relator AS BIGINT), -1),
                    CAST(year_snapshot AS INTEGER)
            ) AS id_pauta,
            CAST(id_evento AS BIGINT)                     AS id_evento,
            CAST(cod_regime AS TEXT)                      AS cod_regime,
            CAST(ordem AS INTEGER)                        AS ordem,
            CAST(id_proposicao AS BIGINT)                 AS id_proposicao,
            TRY_CAST(id_relator AS BIGINT)                AS id_relator,   -- stays NULL if absent
            CAST(year_snapshot AS INTEGER)                AS year_snapshot
        FROM read_csv_auto($path, HEADER=TRUE);
    """, {"path": tf.name})
