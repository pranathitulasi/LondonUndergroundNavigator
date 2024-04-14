# The code reads data form an Excel file and creates a graph using NetworkX
# in this code kruskal's algorithm of find minimum spanning tree
# it basically calculates the shortest distances and the number of stops using Dijkstra's algorithm on the minimum spanning tree
# and last it creates two histograms to visulize the distribution of journey times and the number of stops after closure



import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

dataframe = pd.read_excel('Data.xlsx')             # its just load dataset from an Excel file
dataframe.columns = ["line", "stop1", "stop2", "time"]
dataframe.dropna(inplace=True)

G = nx.Graph()

stop_data = {}                  # it basically create a dictionary to store lines and times associated with stop names

for index, row in dataframe.iterrows():             # iterate through the dataset and add nodes and edges to the graph

    stop1 = row["stop1"]
    stop2 = row["stop2"]
    time = row["time"]
    line = row["line"]

    G.add_node(stop1)           # add the current node to the graph
    G.add_node(stop2)

    G.add_edge(stop1, stop2, weight=time)


minimum_spanning_tree = nx.minimum_spanning_tree(G)         ## here Kruskal's algorithm to find the minimum spanning tree

plt.figure(figsize=(12, 6))


shortest_distances = []
all_stops = list(G.nodes)               #  it just calculate the number of stops using Dijkstra's algorithm on the minimum spanning tree
for i in range(len(all_stops)):
    for j in range(i + 1, len(all_stops)):
        start_stop = all_stops[i]
        end_stop = all_stops[j]
        shortest_distance = nx.shortest_path_length(minimum_spanning_tree, source=start_stop, target=end_stop, weight='weight')
        shortest_distances.append(shortest_distance)

plt.subplot(1, 2, 1)
plt.hist(shortest_distances, bins=25, color='green', edgecolor='black')
plt.xlabel("Journey Times")
plt.ylabel("Frequency Density")
plt.title("Histogram of Journey Times (After Closure)")

num_stops_list = []
all_stops = list(G.nodes)
for i in range(len(all_stops)):
    for j in range(i + 1, len(all_stops)):
        start_stop = all_stops[i]
        end_stop = all_stops[j]
        shortest_path = nx.shortest_path(minimum_spanning_tree, source=start_stop, target=end_stop, weight='weight')
        num_stops = len(shortest_path) - 1  # Number of stops is one less than the length of the path
        num_stops_list.append(num_stops)

plt.subplot(1, 2, 2)
plt.hist(num_stops_list, bins=range(min(num_stops_list), max(num_stops_list) + 2), color='blue', edgecolor='black')
plt.xlabel("Journey Time in Number of Stops")
plt.ylabel("Frequency Density")
plt.title("Histogram of Number of Stops (After Closure)")

plt.tight_layout()              # Create a histogram of the shortest paths
plt.show()
