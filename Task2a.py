# This code is basically counts the number of stations between starting and ending point


from Task1a import readData        #just import the read_data from task1
from dijkstra import dijkstra


def findStops(wb, graph, stop_to_index, start_stop_name, end_stop_name):
    """ This code just uses dijkstra function and counts the number of
    stops between the starting and ending station"""
    start_node = stop_to_index.get(start_stop_name)
    end_node = stop_to_index.get(end_stop_name)

    if start_node is None or end_node is None:              #cheks either inputed stations is in data set or not
        print("Start or end point not is found in the dataset.")
    else:
        d, pi = dijkstra(graph, start_node)
        num_stops = 0
        current_node = end_node
        while current_node != start_node:       #use of while loop for chekcing upto what it should count the stations
            num_stops += 1
            current_node = pi[current_node]
        print(f"Number of stops: {num_stops}")


if __name__ == "__main__":
    wb, graph, stop_to_index, index_to_stop = readData('Data.xlsx')
    start_stop_name = input("Enter the start point: ")
    end_stop_name = input("Enter the end point: ")
    findStops(wb, graph, stop_to_index, start_stop_name, end_stop_name)