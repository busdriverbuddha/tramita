# ### Puxamos da API órgãos que estavam faltando (já verificado)

import httpx
import pandas as pd
import time
# Hardcoded missing orgao IDs
missing = [81, 101347, 382, 79, 6994, 60, 101131, 275, 82, 57, 80, 538490, 538297, 101772, 539426, 539461, 101582, 277, 101489, 102133, 102346, 101798]

# 1) Fetch síncrono com retries e backoff (sem CSVs)
def fetch_one(oid: int, client: httpx.Client, retries: int = 5, backoff_base: float = 1.5):
    for attempt in range(retries):
        try:
            resp = client.get(f"https://dadosabertos.camara.leg.br/api/v2/orgaos/{oid}", timeout=20)
            resp.raise_for_status()
            d = resp.json().get("dados", {})
            # guarda contra payload parcial/malformado
            if not d or "id" not in d:
                return None
            return {
                "id_orgao": int(d["id"]),
                "nome": d.get("nome"),
                "cod_tipo_orgao": int(d["codTipoOrgao"]) if d.get("codTipoOrgao") is not None else None,
                "uri": d.get("uri"),
                "year_snapshot": 2020,
                "rn": 1,
            }
        except Exception:
            # backoff exponencial simples
            time.sleep(backoff_base ** attempt)
    return None

def fetch_all(missing_ids: list[int]):
    rows = []
    with httpx.Client() as client:
        for oid in missing_ids:
            r = fetch_one(oid, client)
            if r is not None:
                rows.append(r)
    return rows

rows = fetch_all(missing)
assert len(rows) > 0, "No rows fetched from API"
df = pd.DataFrame(rows).drop_duplicates(subset=["id_orgao"])

# 2) Register DF in DuckDB and MERGE (insert only the ones not present)
conn.register("orgaos_camara_hotfix", df)

conn.execute("""
    MERGE INTO orgaos_camara AS t
    USING orgaos_camara_hotfix AS s
    ON t.id_orgao = s.id_orgao
    WHEN NOT MATCHED THEN
      INSERT (id_orgao, nome, cod_tipo_orgao, uri, year_snapshot, rn)
      VALUES (s.id_orgao, s.nome, s.cod_tipo_orgao, s.uri, s.year_snapshot, s.rn);
""")

# Optional: clean up registration
try:
    conn.unregister("orgaos_camara_hotfix")
except Exception:
    pass