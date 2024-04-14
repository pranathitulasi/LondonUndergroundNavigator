# The code reads data from an Excel file and creates a graph using NetworkX
#Calculates the shortest distance between all pairs of stops using Dijkstra's algorithmm


import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt     #It uses matplotlib to visulize the distribution of journey times

dataframe = pd.read_excel('Data.xlsx')             # reads data from the excel file
dataframe.columns = ["line", "stop1", "stop2", "time"]
dataframe.dropna(inplace=True)

G = nx.Graph()          # creates an empty graph

stop_data = {}           # creates the dictionary

for index, row in dataframe.iterrows():        # iterates through the dataset and add notes and edges to the graph
    stop1 = row["stop1"]
    stop2 = row["stop2"]
    time = row["time"]
    line = row["line"]

    G.add_node(stop1)
    G.add_node(stop2)

    G.add_edge(stop1, stop2, weight=time)

shortest_distances = []                 # from this part of the code it will calculate the shortest dist. using dijkstra's algo
all_stops = list(G.nodes)
for i in range(len(all_stops)):
    for j in range(i + 1, len(all_stops)):
        start_stop = all_stops[i]
        end_stop = all_stops[j]
        shortest_distance = nx.shortest_path_length(G, source=start_stop, target=end_stop, weight='weight')
        shortest_distances.append(shortest_distance)

plt.hist(shortest_distances, bins=25, color='blue', edgecolor='black') #by using hist() the code is giving output of histogram
plt.xlabel("Journey Times")
plt.ylabel("Frequency Density")
plt.title("Histogram of Journey Times")
plt.show()