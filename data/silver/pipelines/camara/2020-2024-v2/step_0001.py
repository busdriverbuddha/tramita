# # Pipeline prata: Câmara dos Deputados
# 
# Este notebook extrai os dados da fase bronze e popula uma base de dados DuckDB com estes normalizados e deduplicados (ainda sem regularização de chaves estrangeiras)
# # 1. Preparação
# ## 1.1. Imports

import os

from pathlib import Path


import duckdb


from dotenv import load_dotenv

load_dotenv()

DB_PATH = Path(os.getenv("SILVER_DUCKDB_PATH", ""))
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

TMP_DIR = "/tmp/duckdb_tmp"  # make sure it exists

conn = duckdb.connect(DB_PATH)

conn.execute(f"SET temp_directory='{TMP_DIR}'")
conn.execute("SET memory_limit='50GB'")
conn.execute("SET threads=1")
conn.execute("SET preserve_insertion_order=false")
