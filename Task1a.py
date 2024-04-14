#This code basically gives the output of the shortest journey duration in minutes between specified starting and ending destinations


#In this code there are some usage of library codes
import pandas as pd                                     # pandas library is used to enable data and read that data
from dijkstra import dijkstra                           # Dijkstra's algorithm is used because of it makes graph and used for finding the shortest path between nodes in a graph
from adjacency_list_graph import AdjacencyListGraph


def readData(file_path):
    """ This function basically read data from Excel sheet and convert that into dictionary
    which assumes the Excel file has columns named line, stop1, stop2, and time. Then it
    concatenates the stop1 and stop2 columns into single series, and then finds unique stops from
    this Series.
    """
    dataframe = pd.read_excel(file_path)
    dataframe.columns = ["line", "stop1", "stop2", "time"]
    dataframe.dropna(inplace=True)

    all_stops = pd.concat([dataframe['stop1'], dataframe['stop2']], ignore_index=True)  # Concatenates stop1 with stop2

    unique_stops = all_stops.unique()

    stop_to_index = {stop: index + 1 for index, stop in enumerate(unique_stops)}
    index_to_stop = {index: stop for stop, index in stop_to_index.items()}

    dataframe['stop1'] = dataframe['stop1'].map(stop_to_index)                    #maps the stop names in the stop1 and stop2 columns of the dataframe to thier corresponding indices
    dataframe['stop2'] = dataframe['stop2'].map(stop_to_index)

    graph = AdjacencyListGraph(len(unique_stops) + 1, False, True)

    for index, row in dataframe.iterrows():        #iterates through the DataFrame rows
        stop1 = row['stop1']
        stop2 = row['stop2']
        time = row['time']

        try:                                #The try and except block is used to handle any exceptions that may occur during the insertion
            graph.insert_edge(stop1, stop2, weight=time)
        except:
            pass

    return dataframe, graph, stop_to_index, index_to_stop


def findShortestPath(dataframe, graph, stop_to_index, start_stop_name, end_stop_name):
    """ This function basically finds the shortest path by using dijkstra algorithms
    having five parameters"""
    start_node = stop_to_index.get(start_stop_name)
    end_node = stop_to_index.get(end_stop_name)

    if start_node is None or end_node is None:              #it checks if either the starting or ending point is not found in the dataset
        print("Starting or ending point is not found in the dataset.")           #if its not then it should just print out the statement
    else:
        d, pi = dijkstra(graph, start_node)
        print(f"Shortest journey time: {d[end_node]} minutes")          #prints the shortest journey time from the starting node to ending node
        path = [end_node]
        while pi[path[-1]] is not None:             #it just iteratively appending the predecessor of the last node in the path until the starting node is reached and creates the shortest path
            path.append(pi[path[-1]])
        path_names = [index_to_stop[index] for index in reversed(path)]
        print("Shortest path:", " -> ".join(path_names))


if __name__ == "__main__":
    dataframe, graph, stop_to_index, index_to_stop = readData('Data.xlsx')
    start_stop_name = input("Enter the starting point: ")
    end_stop_name = input("Enter the ending point: ")
    findShortestPath(dataframe, graph, stop_to_index, start_stop_name, end_stop_name)