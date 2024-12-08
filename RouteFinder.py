import heapq

## Used CoPilot AI to generate the input.txt file for testing and to help me build the skeleton of this program. 

def read_input(file_name):
    with open(file_name, 'r') as file:
        # Read the number of cities
        n = int(file.readline().strip())

        # Initialize the graph as an adjacency list
        graph = [[] for _ in range(n)]

        # Read the connections
        for line in file:
            # u and v will be the city ID and w for the distance between the two cities. 
            u, v, w = map(int, line.strip().split())
            # Save into memory the city ID's and the distance between them.  
            graph[u].append((v, w))
            graph[v].append((u, w))  
            # Since the graph is undirected, it will need to save the distance from both cities. So from city 0 to 1 and city 1 to 0.

    return graph

    # Use Dijstra's algorithm to find the shortest path between two cities.
def dijkstra(graph, start, end):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    pq = [(0, start)]
    predecessors = [-1] * n

    while pq:
        current_distance, u = heapq.heappop(pq)

        if current_distance > distances[u]:
            continue

        for v, weight in graph[u]:
            distance = current_distance + weight

            if distance < distances[v]:
                distances[v] = distance
                predecessors[v] = u
                heapq.heappush(pq, (distance, v))

    path = []
    node = end
    while node != -1:
        path.append(node)
        node = predecessors[node]

    path.reverse()
    return distances[end], path

def main():
    # Read the input file
    graph = read_input('input.txt')

    # Prompt the user for the start and end cities
    start_city = int(input("Enter the start city ID: "))
    end_city = int(input("Enter the end city ID: "))

    # Find the shortest path using Dijkstra's algorithm
    distance, path = dijkstra(graph, start_city, end_city)

    # Print the result
    print(f"Shortest path from city {start_city} to city {end_city} is {distance} miles.")
    print(f"Path: {' -> '.join(map(str, path))}")

if __name__ == "__main__":
    main()
