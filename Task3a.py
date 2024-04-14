# This code gives same output as Task2 but in this different algorithm is being used

from Task1a import readData                 ## Again read_data is imported from Task1a
from bellman_ford import bellman_ford                   # Have used bellman_ford algorithm from bellman_ford


def revisedShortestPath(wb, graph, stop_to_index, start_stop_name, end_stop_name):
    """This function basically show the number of stops between starting and ending point.
    In this function bellman ford algorithm is used to find the shortest path"""

    start_node = stop_to_index.get(start_stop_name)
    end_node = stop_to_index.get(end_stop_name)

    if start_node is None or end_node is None:              #it checks if either the starting or ending point is not found in the dataset
        print("Start or end point not found in the dataset.")            #if its not then it should just print out the statement
    else:
        d, pi, cycle = bellman_ford(graph, start_node)
        num_stops = 0
        current_node = end_node
        while current_node != start_node:               # use of while loop for checking upto what it should count the stations
            num_stops += 1
            current_node = pi[current_node]
        print(f"Number of stops: {num_stops}")


if __name__ == "__main__":
    wb, graph, stop_to_index, index_to_stop = readData('Data.xlsx')
    start_stop_name = input("Enter the start point: ")
    end_stop_name = input("Enter the end point: ")
    revisedShortestPath(wb, graph, stop_to_index, start_stop_name, end_stop_name)


