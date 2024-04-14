# This code basically shows the output of all the adjecent station which can be closed

from Task1a import readData
from mst import kruskal         #Have used the kruskal algorithm form mst


def convertGraphToEdges(graph):
    """Converts an adjacency list representation of a graph to a list of edges
    and it returns a list of edges, where each edge is represented as tuple in form of (u, v, weight)
    """
    edges = []          #Initialize an empty list to store the edges
    for u in range(graph.get_card_V()):     # iterate through all vertices in the graph
        for edge in graph.get_adj_list(u):          #iterate through all edges adjacent to the current vertex
            v = edge.get_v()                            # get the destination vertex of the edge
            weight = edge.get_weight()                      #get the time of the edge
            edges.append((u, v, weight))            # add the edge to the list of edge
    return edges                    #returns the list of edges


def findAffectedRoutes(original_edges, mst_edges):
    """Finds the affected routes by comparing original and minimum spanning tree edges
    Args:
        original_edges: List of edges from the origingal graph
        mst_edges: List of edges from the minimum spanning tree

    Returns:
        List of affected routes represented as tuples (u, v).
        """
    affected_routes = []        #Initialize an empty list ot store affected routes

    original_set = set(original_edges)          # Convert the original and MST edges to sets for efficient comparison
    mst_set = set(mst_edges)

    closed_edges = original_set - mst_set           # Find the difference between the original edges and MST edges

    for edge in closed_edges:            # Extract affected routes from the closed edges
        u, v, weight = edge
        affected_routes.append((u, v))

    return affected_routes


if __name__ == "__main__":
    wb, graph, stop_to_index, index_to_stop = readData('Data.xlsx')

    minimum_spanning_tree_graph = kruskal(graph)            # Applying Kruskal's algorithm from the mst file to find the minimum spanning tree

    original_edges = convertGraphToEdges(graph)             # Convert the graph to a list of edges
    minimum_spanning_tree_edges = convertGraphToEdges(minimum_spanning_tree_graph)

    affected_routes = findAffectedRoutes(original_edges, minimum_spanning_tree_edges)    # Find the affected routes

    if affected_routes:
        print("Affected Routes:")
        for route in affected_routes:
            u, v = route
            station_u = index_to_stop[u]
            station_v = index_to_stop[v]
            print(f"{station_u} -- {station_v}")
    else:
        print("It's infeasible to meet the closure conditions.")