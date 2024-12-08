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
            # u,v = city ID. w = distance between cities. price = avg. gas price.
            u, v, w, price = line.strip().split()
            u, v, w = int(u), int(v),  int(w)
            price = float(price)
            # Save into memory the city ID's and the distance between them.  
            graph[u].append((v, w, price))
            graph[v].append((u, w, price))  
            # Since the graph is undirected, it will need to save the distance from both cities. So from city 0 to 1 and city 1 to 0.

    return graph

    # Use Dijstra's algorithm to find the shortest path between two cities.
def dijkstra(graph, start, end, gasTank, gasEff):
    n = len(graph)
    distances = [float('inf')] * n
    costs = [float('inf')] * n
    distances[start] = 0
    costs[start] = 0
    pq = [(0, 0, start)]
    predecessors = [-1] * n

    while pq:
        current_distance, current_cost, u = heapq.heappop(pq)

        if current_distance > distances[u] and current_cost > costs[u]:
            continue

        for v, weight, price in graph[u]:
            distance = current_distance + weight
            cost = current_cost
            gas_needed = weight / gasEff

            if gas_needed > gasTank:
                # Check if the car will need to refill during the trip.
                refills_needed = int(gas_needed // gasTank)
                remaining_distance = gas_needed % gasTank
                total_cost = refills_needed * gasTank * price + remaining_distance * price
            else:
                # Only one refill or no refill needed
                total_cost = gas_needed * price
            
            cost += total_cost

            if distance < distances[v] or cost < costs[v]:
                distances[v] = distance
                costs[v] = cost
                predecessors[v] = u
                heapq.heappush(pq, (distance, cost, v))

    path = []
    node = end
    while node != -1:
        path.append(node)
        node = predecessors[node]

    path.reverse()
    return distances[end], costs[end], path

def main():
    # Define car characteristics
    gasTank = 14  
    gasLevel = 100.0 
    gasEff = 12
    
    # Read the input file
    graph = read_input('input.txt')

    # Prompt the user for the start and end cities
    start_city = int(input("Enter the start city ID: "))
    end_city = int(input("Enter the end city ID: "))

    # Find the shortest and cheapest path using Dijkstra's algorithm
    distance, cost, path = dijkstra(graph, start_city, end_city, gasTank, gasEff)

    # Print the result
    print(f"Shortest path from city {start_city} to city {end_city} is {distance} miles with a cost of ${cost:.2f}.")
    print(f"Path: {' -> '.join(map(str, path))}")

if __name__ == "__main__":
    main()
