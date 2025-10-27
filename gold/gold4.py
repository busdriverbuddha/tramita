
import os

from pathlib import Path

import duckdb
import numpy as np
import pandas as pd
import igraph as ig

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

# with duckdb.connect(DB_PATH, read_only=True) as con:

def merge_nodes(nodes_df: pd.DataFrame, edges_df: pd.DataFrame, taglist: list[str]) -> None:
    surviving_tag = taglist[0]
    for removed_tag in taglist[1:]:
        edges_df.loc[edges_df['source'] == removed_tag, 'source'] = surviving_tag
        edges_df.loc[edges_df['target'] == removed_tag, 'target'] = surviving_tag

    nodes_df.drop(index=taglist[1:], inplace=True)
    

def prune_graph(node_df: pd.DataFrame, edge_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    def _prune_nodes(node_df: pd.DataFrame, edge_df: pd.DataFrame) -> pd.DataFrame:
        return node_df[
            (node_df['name'].isin(edge_df['from']))
            | (node_df['name'].isin(edge_df['to']))
        ]
        
        
    def _prune_edges(node_df: pd.DataFrame, edge_df: pd.DataFrame) -> pd.DataFrame:
        return edge_df[
            (edge_df['from'].isin(node_df['name']))
            & (edge_df['to'].isin(node_df['name']))
        ]

    while True:
        n = len(node_df)
        m = len(edge_df)
        node_df = _prune_nodes(node_df, edge_df)
        edge_df = _prune_edges(node_df, edge_df)
        if n == len(node_df) and m == len(edge_df):
            return node_df, edge_df
        
def build_graph(node_df: pd.DataFrame, edge_df: pd.DataFrame) -> ig.Graph:
    edge_tuples = list(zip(edge_df['from'], edge_df['to']))
    g = ig.Graph.TupleList(
        edge_tuples,
        directed=False,
        vertex_name_attr="name",
        weights=True,
    )
    for col in node_df.columns:
        if col != "name":
            g.vs[col] = node_df.set_index("name").loc[g.vs['name'], col].tolist()

    for col in edge_df.columns:
        if col not in ("from", "to"):
            g.es[col] = edge_df[col].tolist()
    
    return g

def get_community(g: ig.Graph) -> ig.VertexClustering:
    community_method = None
    try:
        cl = g.community_leiden(objective_function="modularity")
        community_method = "leiden"
    except Exception:
        cl = g.community_multilevel()  # Louvain
        community_method = "louvain"
    
    print(f"Community method used: {community_method}")
    return cl

def get_metrics(g: ig.Graph) -> pd.DataFrame:
    vcount = g.vcount()
    components = g.components()
    component_sizes = pd.Series([len(c) for c in components], name="size").to_frame()
    component_sizes["component_id"] = component_sizes.index
    component_sizes = component_sizes[["component_id","size"]].sort_values("size", ascending=False).reset_index(drop=True)
    
    comp_id_map = {}
    for cid, comp in enumerate(components):
        for vid in comp:
            comp_id_map[vid] = cid
    
    degree_all = g.degree()
    eigenvector = g.eigenvector_centrality()

    return pd.DataFrame({
        "id":                 g.vs["name"],
        "type":               g.vs["type"],
        "label": g.vs["label"],
        "degree":             degree_all,
        "eigenvector":        eigenvector,
        "component_id":       [comp_id_map[i] for i in range(vcount)],
    })
    
def top_n(df: pd.DataFrame, col: str, n: int = 10, node_types: list | None = None) -> pd.DataFrame:
    sub = df if node_types is None else df[df["type"].isin(node_types)]
    return sub.sort_values(col, ascending=False).head(n).reset_index(drop=True)


event_df = pd.read_pickle("full_event_df.pkl")
event_df

edges_df = pd.read_parquet(EDGES_PATH_PARQUET)
nodes_df = pd.read_parquet(NODES_PATH_PARQUET)

# agregamos as autorias aos eventos

event_labeled_df = event_df.join(
    edges_df[edges_df['etype'] == 'autoria'].set_index('target')[['source']], on="prop_tag"
).rename(columns={'source': 'auth_camara_tag'}).join(
    edges_df[edges_df['etype'] == 'autoria'].set_index('target')[['source']], on="proc_tag"
).rename(columns={'source': 'auth_senado_tag'}).join(
    nodes_df.set_index('tag')[['label']], on="auth_camara_tag", rsuffix="_auth"
).rename(columns={'label_auth': 'auth_camara_label'}).join(
    nodes_df.set_index('tag')[['label']], on="auth_senado_tag", rsuffix="_auth"
).rename(columns={'label_auth': 'auth_senado_label'})
event_labeled_df

# como agora temos uma fileira para cada autor, vamos manter apenas o primeiro (só precisamos saber de onde sai cada projeto)

event_labeled_df = event_labeled_df[event_labeled_df[['label', 'event_ts', 'event', 'event_loc']].ne(
    event_labeled_df[['label', 'event_ts', 'event', 'event_loc']].shift()
).any(axis=1)].reset_index(drop=True)

for col in event_labeled_df.columns:
    if col.endswith("_tag"):
        event_labeled_df[col] = event_labeled_df[col].str.strip().str.upper()

event_labeled_df = event_labeled_df.fillna('')

from_camara = (
    event_labeled_df['auth_camara_tag'].str.startswith("CD:")
    | (event_labeled_df['auth_senado_tag'] == "SE:2")
    | (event_labeled_df['auth_camara_tag'].isin([
        "CO:5438",  # Comissão de Legislação Participativa
        "CO:2003",  # CCJC
        "CO:539426",  # CPI da Americanas
    ]))
    | (event_labeled_df['auth_camara_label'].str.startswith("Comissão Mista da MPV"))  # Todas começam na Câmara
)
from_senado = (
    event_labeled_df['auth_senado_tag'].str.startswith("SS:")
    | (event_labeled_df['auth_camara_tag'].isin([
        "CO:78",  # Senado
        "CO:79",  # Comissão mista (na verdade o autor é o Sen. Jorginho Mello)
    ]))
    | (event_labeled_df['auth_senado_tag'].isin([
        "SE:7352398",  # CPI da Pandemia
        "SE:3947422",  # Comissão de direitos humanos do Senado 
    ]))
)
from_externo = ~(from_camara | from_senado)

event_labeled_df['origem'] = np.select(
    [from_camara, from_senado, from_externo],
    ['camara', 'senado', 'externo'],
    default='unknown'
)
event_labeled_df

event_labeled_df

# Vamos certificar que os externos realmente são externos

event_labeled_df[event_labeled_df['origem'] == 'externo'][[c for c in event_labeled_df.columns if c.startswith("auth")]].value_counts()

# Critérios para score de proposições:
# 
# (considerando que o caminho pode ser Câmara -> Senado ou Senado -> Câmara)
# 
# * Foi protocolada na primeira casa mas não chegou a comissão ou plenário: 0.0
# * Chegou a comissão ou plenário na primeira casa: 0.25
# * Aprovada na primeira casa: 0.5
# * Chegou a comissão ou plenário na segunda casa: 0.75
# * Aprovada na segunda casa (ou seja, remetida a sanção ou promulgação): 1.0


df = event_labeled_df
by_label = df.groupby('label', sort=False)
origem = by_label['origem'].first()
origem

is_mpv_pl = df['label'].str.startswith(('MPV','PL'))
is_pec = df['label'].str.startswith('PEC')
has_sancao = df['event'].eq(Event.REMETIDO_A_SANCAO).groupby(df['label']).any()
has_promulg = df['event'].eq(Event.REMETIDO_A_PROMULGACAO).groupby(df['label']).any()

presence = (
    df.assign(present=True)
      .pivot_table(index='label',
                   columns=['casa','event'],
                   values='present',
                   aggfunc='any',
                   fill_value=False)
)
presence

def P(house: str, event: Event) -> pd.Series:
    col = (house, event)
    return presence[col] if col in presence.columns else pd.Series(False, index=presence.index)


score_camara_externo = np.select(
    [
        (is_mpv_pl.groupby(df['label']).any() & has_sancao) |
        (is_pec.groupby(df['label']).any() & has_promulg),  # 1.0
        P('senado', Event.RECEBIDO_COMISSAO) | P('senado', Event.APROVADA_URGENCIA) | P('senado', Event.DESIGNADO_RELATOR_PLENARIO),  # 0.75
        P('camara', Event.APROVADO_PLENARIO),  # 0.5
        P('camara', Event.RECEBIDO_COMISSAO) | P('camara', Event.APROVADA_URGENCIA) | P('camara', Event.DESIGNADO_RELATOR_PLENARIO),  # 0.25
    ],
    [1.0, 0.75, 0.50, 0.25],
    default=0.0
)

score_senado = np.select(
    [
        (is_mpv_pl.groupby(df['label']).any() & has_sancao) |
        (is_pec.groupby(df['label']).any() & has_promulg),  # 1.0
        P('camara', Event.RECEBIDO_COMISSAO) | P('camara', Event.APROVADA_URGENCIA) | P('camara', Event.DESIGNADO_RELATOR_PLENARIO),  # 0.75
        P('senado', Event.APROVADO_PLENARIO),  # 0.5
        P('senado', Event.RECEBIDO_COMISSAO) | P('senado', Event.APROVADA_URGENCIA) | P('senado', Event.DESIGNADO_RELATOR_PLENARIO),  # 0.25
    ],
    [1.0, 0.75, 0.50, 0.25],
    default=0.0
)

scores = pd.DataFrame({
    'origem': origem,
    'score_camara_externo': score_camara_externo,
    'score_senado': score_senado,
})
scores['score'] = np.where(
    scores['origem'].isin(['camara','externo']),
    scores['score_camara_externo'],
    np.where(scores['origem'].eq('senado'), scores['score_senado'], np.nan)
)

labels_and_scores: list[dict] = (
    scores['score']
    .rename('score')
    .to_frame()
    .reset_index(names='label')
    .to_dict('records')
)

labels_and_scores_df = pd.DataFrame(labels_and_scores).set_index('label', drop=True)
labels_and_scores_df

nodes_scored_df = nodes_df.join(labels_and_scores_df, on="label")
nodes_scored_df = nodes_scored_df.set_index('tag', drop=True)
nodes_scored_df

edges_df

nodes_scored_df

edges_df

from collections import defaultdict

ccs: dict[str, set] = defaultdict(set)

for index, row in edges_df[edges_df['etype'].eq('correspondencia')].iterrows():
    src = row['source']
    tgt = row['target']
    src_set = ccs[src]
    tgt_set = ccs[tgt]
    new_set = {src, tgt}
    if not src_set and not tgt_set:
        ccs[src] = new_set
        ccs[tgt] = new_set
    elif not src_set:
        tgt_set.update(new_set)    
        ccs[src] = tgt_set
    else:  # no tgt_set
        src_set.update(new_set)
        ccs[tgt] = src_set
    

unique_ccs = {frozenset(s) for s in ccs.values()}

nodes_to_merge = [sorted(s) for s in unique_ccs]


edges_auth_df = edges_df[edges_df['etype'].eq('autoria')].drop(['etype'], axis=1).copy()

for taglist in nodes_to_merge:
    merge_nodes(nodes_scored_df, edges_auth_df, taglist)

nodes_scored_df

edges_weighted_df = edges_auth_df.join(nodes_scored_df[['score']], on="target").rename(columns={'score': 'weight'})

edge_df = edges_weighted_df.rename(columns={'source': 'from', 'target': 'to'})
edge_df.head()

node_df = nodes_scored_df.reset_index().rename(columns={'tag': 'name'})
node_df.head()



node_df, edge_df = prune_graph(node_df, edge_df)

# Finalmente, a partir deste ponto não existe mais diferença entre um órgão ou ente (nomes diferentes para a mesma coisa)
node_df.loc[node_df['type'] == "Ente", 'type'] = 'Orgao'

node_df.value_counts('type')

type_to_bigtype = {
    'Proposicao': 'bill',
    'Processo': 'bill',
    'Orgao': 'author',
    'Deputado': 'author',
    'Senador': 'author',
}

node_df['bigtype'] = node_df['type'].map(type_to_bigtype)
node_df.value_counts('bigtype')

# # Análises

# ## Escore médio por autor (mais simples)

author_mean_scores = (edge_df.groupby('from', as_index=False)['weight'].mean().rename(
    columns={'from': 'author', 'weight': 'mean_score'}  # type: ignore
).set_index('author', drop=True))
author_mean_scores

author_bill_counts = edge_df['from'].value_counts().rename_axis('name').reset_index(name='from_count').set_index('name', drop=True)

author_performance_df = node_df.join(author_mean_scores, on="name", how="inner").drop("score", axis=1).join(author_bill_counts, on="name", how="inner").set_index('name', drop=True)
author_performance_df

# "Melhores" deputados
author_performance_df[author_performance_df['type'].eq("Deputado")].sort_values("mean_score", ascending=False)

# "Melhores" senadores
author_performance_df[author_performance_df['type'].eq("Senador")].sort_values("mean_score", ascending=False)

# "Melhores" órgãos ou entes
author_performance_df[author_performance_df['type'].eq("Orgao")].sort_values("mean_score", ascending=False)

# Vemos que acabam sendo privilegiados parlamentares/órgãos que participaram de poucos projetos bem-sucedidos. Vamos penalizar por número de tentativas.

means_by_type = {
    t: author_performance_df[author_performance_df['type'].eq(t)]['from_count'].mean()
    for t in author_performance_df['type'].unique()
}
means_by_type

author_performance_df['concave_score'] = (
    author_performance_df['mean_score']
    * author_performance_df['from_count'] / (author_performance_df['from_count'] + author_performance_df['type'].apply(lambda v: means_by_type[v])))

# "Melhores" deputados
author_performance_df[author_performance_df['type'].eq("Deputado")].sort_values("concave_score", ascending=False)

# "Melhores" senadores
author_performance_df[author_performance_df['type'].eq("Senador")].sort_values("concave_score", ascending=False)

# "Melhores" orgaos
author_performance_df[author_performance_df['type'].eq("Orgao")].sort_values("concave_score", ascending=False)

# Tudo isso é subjetivo e senende da nossa definição de sucesso, é claro. Vamos tentar uma abordagem por grafo.
# Vamos verificar a centralidade por autovetores, usando o score das proposições como pesos nas arestas.


g = build_graph(node_df, edge_df)
vertex_metrics = get_metrics(g)
top10_deps_eigen = top_n(vertex_metrics, "eigenvector", 10, node_types=["Deputado"])
top10_sens_eigen = top_n(vertex_metrics, "eigenvector", 10, node_types=["Senador"])
top10_orgs_eigen = top_n(vertex_metrics, "eigenvector", 10, node_types=["Orgao"])


top10_deps_eigen

top10_sens_eigen

top10_orgs_eigen

# ## Análises por tipo de proposição
# 
# Entendemos que PLs, PECs e MPs têm naturezas muito diferentes e faria mais sentido analisá-las em separado

node_df.shape, edge_df.shape



pl_node_df = node_df[(node_df['label'].str.startswith("PL"))|(node_df['bigtype'].ne('bill'))].copy()
pl_node_df, pl_edge_df = prune_graph(pl_node_df, edge_df.copy())
pl_node_df


pl_g = build_graph(pl_node_df, pl_edge_df)
pl_vertex_metrics = get_metrics(pl_g)
top10_deps_eigen = top_n(pl_vertex_metrics, "eigenvector", 10, node_types=["Deputado"])
top10_sens_eigen = top_n(pl_vertex_metrics, "eigenvector", 10, node_types=["Senador"])
top10_orgs_eigen = top_n(pl_vertex_metrics, "eigenvector", 10, node_types=["Orgao"])

top10_deps_eigen

top10_sens_eigen

top10_orgs_eigen

pec_node_df = node_df[(node_df['label'].str.startswith("PEC"))|(node_df['bigtype'].ne('bill'))].copy()
pec_node_df, pec_edge_df = prune_graph(pec_node_df, edge_df.copy())
pec_g = build_graph(pec_node_df, pec_edge_df)
pec_vertex_metrics = get_metrics(pec_g)
top10_deps_eigen = top_n(pec_vertex_metrics, "eigenvector", 10, node_types=["Deputado"])
top10_sens_eigen = top_n(pec_vertex_metrics, "eigenvector", 10, node_types=["Senador"])
top10_orgs_eigen = top_n(pec_vertex_metrics, "eigenvector", 10, node_types=["Orgao"])

top10_deps_eigen

top10_sens_eigen

top10_orgs_eigen

# (para medidas provisórias, é claro, esta análise não cabe, pois a autoria é sempre do Poder Executivo)

# ## Análise por casa legislativa

dep_node_df = node_df[(node_df['name'].str.startswith("CD:"))|(node_df['bigtype'].ne('author'))].copy()
dep_node_df, dep_edge_df = prune_graph(dep_node_df, edge_df.copy())
dep_g = build_graph(dep_node_df, dep_edge_df)
dep_vertex_metrics = get_metrics(dep_g)
top10_deps_eigen = top_n(dep_vertex_metrics, "eigenvector", 10, node_types=["Deputado"])

top10_deps_eigen

sen_node_df = node_df[(node_df['name'].str.startswith("SS:"))|(node_df['bigtype'].ne('author'))].copy()
sen_node_df, sen_edge_df = prune_graph(sen_node_df, edge_df.copy())
sen_g = build_graph(sen_node_df, sen_edge_df)
sen_vertex_metrics = get_metrics(sen_g)
top10_sens_eigen = top_n(sen_vertex_metrics, "eigenvector", 10, node_types=["Senador"])

top10_sens_eigen

# # Análise por comunidade

g.vs['bigtype_bool'] = [t == 'author' for t in g.vs['bigtype']]

g_bill, g_auth = g.bipartite_projection(
    types='bigtype_bool',
    multiplicity=True,  # queremos + arestas por parceria
)

g_auth.vs['score'][:10]

cl = get_community(g_auth)

cl.modularity

vertex_metrics = get_metrics(g_auth)
top10_deps_eigen = top_n(vertex_metrics, "eigenvector", 10, node_types=["Deputado"])
top10_sens_eigen = top_n(vertex_metrics, "eigenvector", 10, node_types=["Senador"])
top10_orgs_eigen = top_n(vertex_metrics, "eigenvector", 10, node_types=["Orgao"])

top10_deps_eigen

top10_sens_eigen

top10_orgs_eigen





import pandas as pd
import igraph as ig
from itertools import combinations

def author_projection_sum_scores(edges_df: pd.DataFrame, nodes_df) -> ig.Graph:
    """
    Build an author-author projection where edge weight(i,j) = sum of scores of bills
    co-authored by i and j. Assumes 'weight' on each (author,bill) row equals the bill's score.
    """
    # ensure types
    df = edges_df[['from','to','weight']].copy()
    df['from'] = df['from'].astype(str)
    df['to']   = df['to'].astype(str)
    df['weight'] = df['weight'].astype(float)

    # Aggregate per bill: list authors and the bill's score (assumed constant within bill)
    per_bill = (df.groupby('to')
                  .agg(authors=('from', lambda s: sorted(pd.unique(s))),
                       score=('weight', 'first'))
                  .reset_index())

    # Build pair weights by summing scores over shared bills
    pair_rows: list[tuple[str,str,float]] = []
    for _, row in per_bill.iterrows():
        authors = row['authors']
        s = float(row['score'])
        if len(authors) >= 2:
            for a, b in combinations(authors, 2):
                pair_rows.append((a, b, s))

    if not pair_rows:
        # No co-authorships; return empty graph with isolated author nodes
        authors_all = df['from'].unique().tolist()
        g_auth = ig.Graph()
        g_auth.add_vertices(authors_all)
        g_auth.vs['name'] = authors_all
        return g_auth

    pair_df = pd.DataFrame(pair_rows, columns=['a','b','w']).groupby(['a','b'], as_index=False)['w'].sum()

    # Create igraph author-author weighted graph
    authors_all = pd.Index(pd.unique(df['from'])).tolist()
    name_to_vid = {name: i for i, name in enumerate(authors_all)}

    edges = [(name_to_vid[a], name_to_vid[b]) for a,b in pair_df[['a','b']].to_numpy()]
    weights = pair_df['w'].to_numpy().tolist()

    g_auth = ig.Graph(n=len(authors_all), edges=edges, directed=False)
    g_auth.vs['name'] = authors_all
    g_auth.vs['label'] = nodes_df.set_index('name').loc[authors_all, 'label']
    g_auth.vs['partido'] = nodes_df.set_index('name').loc[authors_all, 'partido']
    g_auth.vs['score'] = nodes_df.set_index('name').loc[authors_all, 'score']
    g_auth.vs['type'] = nodes_df.set_index('name').loc[authors_all, 'type']
    g_auth.es['weight'] = weights
    return g_auth


auth_score_g = author_projection_sum_scores(edge_df, node_df)

cl = get_community(auth_score_g)

cl.modularity

vertex_metrics = get_metrics(auth_score_g)
top10_deps_eigen = top_n(vertex_metrics, "eigenvector", 10, node_types=["Deputado"])
top10_sens_eigen = top_n(vertex_metrics, "eigenvector", 10, node_types=["Senador"])
top10_orgs_eigen = top_n(vertex_metrics, "eigenvector", 10, node_types=["Orgao"])

top10_deps_eigen

top10_sens_eigen

top10_orgs_eigen

node_df

import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

# g: your igraph.Graph with vertex attributes:
# - 'type' (str) -> node type
# - optional 'weight' on edges

def view_graph(g: ig.Graph):
    # 1) Layout + communities
    layout = g.layout_fruchterman_reingold(weights=g.es['weight'] if 'weight' in g.es.attributes() else None, niter=2000)
    coords = np.array(layout.coords)

    # Leiden communities (falls back if package not installed)
    try:
        comm = g.community_leiden(objective_function='modularity', weights=g.es['weight'] if 'weight' in g.es.attributes() else None)
    except Exception:
        comm = g.community_multilevel(weights=g.es['weight'] if 'weight' in g.es.attributes() else None)

    # 2) Colors by node type
    types = [v['type'] for v in g.vs]
    uniq_types = sorted(set(types))
    palette = plt.cm.get_cmap('tab10', len(uniq_types))
    color_map = {t: palette(i) for i, t in enumerate(uniq_types)}
    vcolors = [color_map[t] for t in types]

    # 3) Plot nodes & edges with matplotlib for full control
    fig, ax = plt.subplots(figsize=(10, 10))
    # edges
    for e in g.es:
        i, j = e.tuple
        ax.plot([coords[i,0], coords[j,0]], [coords[i,1], coords[j,1]], lw=0.4, alpha=0.25, zorder=1)

    # nodes
    ax.scatter(coords[:,0], coords[:,1], s=15, c=vcolors, edgecolors='white', linewidths=0.4, zorder=2)

    # 4) (Optional) draw translucent hulls per community
    for cid in range(len(comm)):
        members = np.array(comm.membership) == cid
        pts = coords[members]
        if pts.shape[0] >= 3:
            hull = ConvexHull(pts)
            poly = plt.Polygon(pts[hull.vertices], alpha=0.08, ec='none', fc='gray')
            ax.add_patch(poly)

    # 5) Legend for node types
    handles = [plt.Line2D([0],[0], marker='o', linestyle='', markersize=8, markerfacecolor=color_map[t], markeredgecolor='white') for t in uniq_types]
    ax.legend(handles, uniq_types, frameon=False, loc='upper right', title='Node type')

    ax.set_axis_off()
    plt.tight_layout()
    plt.show()


node_df

house_node_df = node_df[(node_df['name'].str.startswith('CD:'))|(node_df['bigtype'].eq('bill'))]
house_node_df, house_edge_df = prune_graph(house_node_df, edge_df)
house_node_df.shape, house_edge_df.shape

g = build_graph(house_node_df, house_edge_df)

view_graph(g)

