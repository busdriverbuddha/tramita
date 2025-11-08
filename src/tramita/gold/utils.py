import pandas as pd
import igraph as ig


def build_graph(
    node_df: pd.DataFrame,
    edge_df: pd.DataFrame,
    source_tag: str = "from",
    target_tag: str = "to",
    name_tag: str = "name",
) -> ig.Graph:
    """
    Builds an igraph.Graph from a node and edge list.
    The node DataFrame must have a 'name' column with the unique identifiers.
    The edge DataFrame must have 'from' and 'to' columns.
    Any other columns will be absorbed as attributes.
    """
    node_df = node_df.copy()
    edge_df = edge_df.copy()

    if source_tag != "from" or target_tag != "to":
        edge_df = edge_df.rename(columns={
            source_tag: "from",
            target_tag: "to",
        })
    
    if name_tag != "name":
        node_df = node_df.rename(columns={name_tag: "name"})

    edge_tuples: list[tuple[str, str]] = list(zip(edge_df['from'], edge_df['to']))

    g = ig.Graph.TupleList(
        edge_tuples,
        directed=False,
        vertex_name_attr="name",
        weights=True,
    )
    
    tag_list: list[str] = g.vs['name']
    for col in node_df.columns:
        if col != "name":
            g.vs[col] = node_df.set_index("name").loc[tag_list, col].tolist()

    for col in edge_df.columns:
        if col not in ("from", "to"):
            g.es[col] = edge_df[col].tolist()
    
    return g


def merge_nodes(nodes_df: pd.DataFrame, edges_df: pd.DataFrame, taglist: list[str]) -> None:
    """Merges the indicated nodes and consolidates the respective edges."""
    surviving_tag = taglist[0]
    for removed_tag in taglist[1:]:
        edges_df.loc[edges_df['source'] == removed_tag, 'source'] = surviving_tag
        edges_df.loc[edges_df['target'] == removed_tag, 'target'] = surviving_tag

    nodes_df.drop(index=taglist[1:], inplace=True)
    

def prune_graph(
    node_df: pd.DataFrame,
    edge_df: pd.DataFrame,
    tag_col: str = "name",
    from_col: str = "from",
    to_col: str = "to",
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Removes any orphan nodes, then edges, until every node has degree at least 1."""
    def _prune_nodes(node_df: pd.DataFrame, edge_df: pd.DataFrame) -> pd.DataFrame:
        return node_df[
            (node_df[tag_col].isin(edge_df[from_col]))
            | (node_df[tag_col].isin(edge_df[to_col]))
        ]
        
        
    def _prune_edges(node_df: pd.DataFrame, edge_df: pd.DataFrame) -> pd.DataFrame:
        return edge_df[
            (edge_df[from_col].isin(node_df[tag_col]))
            & (edge_df[to_col].isin(node_df[tag_col]))
        ]

    while True:
        n = len(node_df)
        m = len(edge_df)
        node_df = _prune_nodes(node_df, edge_df)
        edge_df = _prune_edges(node_df, edge_df)
        if n == len(node_df) and m == len(edge_df):
            return node_df, edge_df
       
        
def add_column_from_graph(g: ig.Graph, df: pd.DataFrame, attr_name: str) -> pd.DataFrame:
    return df.join(
        pd.DataFrame([{'name': v['name'], attr_name: v[attr_name]} for v in g.vs]).set_index('name', drop=True),
        on="name"
    )
