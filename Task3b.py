# The code reads data from an Excel file and creates a graph using NetworkX
#Calculates the shortest distance between all pairs of stops using the bellman-ford algorithm

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

dataframe = pd.read_excel('Data.xlsx')
dataframe.columns = ["line", "stop1", "stop2", "time"]
dataframe.dropna(inplace=True)

G = nx.Graph()

stop_data = {}

for index, row in dataframe.iterrows():
    stop1 = row["stop1"]
    stop2 = row["stop2"]
    time = row["time"]
    line = row["line"]

    G.add_node(stop1)
    G.add_node(stop2)

    G.add_edge(stop1, stop2, weight=time)


num_stops_list = []             # Calculate the number of stops using Bellman-Ford algorithm
all_stops = list(G.nodes)
for i in range(len(all_stops)):
    for j in range(i + 1, len(all_stops)):
        start_stop = all_stops[i]
        end_stop = all_stops[j]

        if nx.has_path(G, source=start_stop, target=end_stop):
            shortest_path_length = nx.bellman_ford_path_length(G, source=start_stop, target=end_stop, weight='weight')
            num_stops = int(shortest_path_length)  # Convert path length to an integer for the number of stops
            num_stops_list.append(num_stops)


plt.hist(num_stops_list, bins=range(min(num_stops_list), max(num_stops_list) + 2), color='blue', edgecolor='black')
plt.xlabel("Journey Time in Number of Stops")
plt.ylabel("Frequency Density")
plt.title("Histogram of Number of Stops (Bellman-Ford)")
plt.show()