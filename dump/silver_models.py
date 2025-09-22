import pyarrow.parquet as pq
import json
import pandas as pd
import tempfile
from glob import glob

paths = glob("data/bronze/snapshots/bronze-2020-smoke/camara/relacionadas/year=*/part-*.parquet")

with tempfile.NamedTemporaryFile() as tf:

    table = pq.read_table(paths)
    df = table.to_pandas()

    df.head()
    exploded_rows = []

    for index, row in df.iterrows():
        payload = json.loads(row['payload_json'])
        for item in payload['dados']:
            exploded_rows.append({
                'id_proposicao_origem': row['id'],
                'id_proposicao_destino': item['id'],
                'year_snapshot': row['year'],
            })
    exploded_df = pd.DataFrame(exploded_rows)
    exploded_df.to_csv(tf.name)

    conn.execute(f"""
        DROP TABLE IF EXISTS relacionadas_camara;
        CREATE TABLE relacionadas_camara AS
            SELECT
                id_proposicao_origem::BIGINT AS id_proposicao_origem,
                id_proposicao_destino::BIGINT AS id_proposicao_destino,
                year_snapshot::INTEGER AS year_snapshot
            FROM read_csv_auto('{tf.name}', HEADER=TRUE);
    """)