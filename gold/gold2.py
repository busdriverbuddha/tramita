# # 2. Análise inicial
# 
# ## 2.1. Imports

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

# ## 2.1. Instanciamento do grafo

edges_df = pd.read_csv(EDGES_PATH_CSV)
edges_df = edges_df.rename(columns={'source': 'from', 'target': 'to'})
edges_df.head()


nodes_df = pd.read_csv(NODES_PATH_CSV)
nodes_df = nodes_df.rename(columns={"tag": "name"})
nodes_df.head()

edge_tuples = list(zip(edges_df['from'], edges_df['to']))
g = ig.Graph.TupleList(
    edge_tuples,
    directed=False,
    vertex_name_attr="name"
)

for col in nodes_df.columns:
    if col != "name":
        g.vs[col] = nodes_df.set_index("name").loc[g.vs["name"], col].tolist()

for col in edges_df.columns:
    if col not in ("from", "to"):
        g.es[col] = edges_df[col].tolist()

print(g.summary())

summary = g.summary()
vcount, ecount = g.vcount(), g.ecount()
density = g.density()
components = g.components()
component_sizes = pd.Series([len(c) for c in components], name="size").to_frame()
component_sizes["component_id"] = component_sizes.index
component_sizes = component_sizes[["component_id","size"]].sort_values("size", ascending=False).reset_index(drop=True)

print(f"|V| = {vcount}")
print(f"|E| = {ecount}")
print(f"Densidade: {density}")
print(f"{len(components)} componentes conexos.")
component_sizes

comp_id_map = {}
for cid, comp in enumerate(components):
    for vid in comp:
        comp_id_map[vid] = cid
        
degree_all   = g.degree()
eigenvector  = g.eigenvector_centrality()
community_method = None
cl = g.community_leiden(objective_function="modularity")
membership = cl.membership
vertex_metrics = pd.DataFrame({
    "id":                 g.vs["name"],
    "type":               g.vs["type"],
    "label": g.vs["label"],
    "degree":             degree_all,
    "eigenvector":        eigenvector,
    "community_id":       membership,
    "component_id":       [comp_id_map[i] for i in range(vcount)],
})

def top_n(df: pd.DataFrame, col: str, n: int = 10, node_types: list | None = None) -> pd.DataFrame:
    sub = df if node_types is None else df[df["type"].isin(node_types)]
    return sub.sort_values(col, ascending=False).head(n).reset_index(drop=True)


top10_deps_eigen = top_n(vertex_metrics, "eigenvector", 10, node_types=["Deputado"])
top10_sens_eigen = top_n(vertex_metrics, "eigenvector", 10, node_types=["Senador"])
top10_orgs_eigen = top_n(vertex_metrics, "eigenvector", 10, node_types=["Orgao"])
top10_ents_eigen = top_n(vertex_metrics, "eigenvector", 10, node_types=["Ente"])


top10_deps_eigen

top10_sens_eigen

top10_orgs_eigen

top10_ents_eigen