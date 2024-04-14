# The code basically reads data from a Excel file and creates a graph using NetworkX
#Calculate the number stops in the shortest path between all pairs of stops

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt         #the use of matplotlib to visualize the distribution of the number of stops in journey times


dataframe = pd.read_excel('Data.xlsx')          # it will read data from dataset
dataframe.columns = ["line", "stop1", "stop2", "time"]      #rename columns for the consistency
dataframe.dropna(inplace=True)              #drop rows with missing values

G = nx.Graph()              # Create a graph

stop_data = {}              # create a dictionary to store lines and times associated with stop names

for index, row in dataframe.iterrows():         # iterate through the dataset and add nodes and edges to the graph

    stop1 = row["stop1"]
    stop2 = row["stop2"]
    time = row["time"]
    line = row["line"]

    G.add_node(stop1)                   # this add the current node to the graph
    G.add_node(stop2)

    G.add_edge(stop1, stop2, weight=time)


num_stops_list = []             # Calculate the number of stops using Dijkstra's algorithm
all_stops = list(G.nodes)
for i in range(len(all_stops)):
    for j in range(i + 1, len(all_stops)):
        start_stop = all_stops[i]
        end_stop = all_stops[j]
        shortest_path = nx.shortest_path(G, source=start_stop, target=end_stop, weight='weight')
        num_stops = len(shortest_path) - 1  # Number of stops is one less than the length of the path
        num_stops_list.append(num_stops)


plt.hist(num_stops_list, bins=range(min(num_stops_list), max(num_stops_list) + 2), color='blue', edgecolor='black')         # Create a histogram of the number of stops
plt.xlabel("Journey Time in Number of Stops")
plt.ylabel("Frequency Density")
plt.title("Histogram of Number of Stops")
plt.show()
