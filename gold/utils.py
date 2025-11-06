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
