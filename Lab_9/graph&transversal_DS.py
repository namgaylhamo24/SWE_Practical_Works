from collections import deque

# Step 1: Implement the Graph Class
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

    # Step 2: Implement Depth-First Search (DFS)
    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)
    
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    # Step 3: Implement Breadth-First Search (BFS)
    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    # Step 4: Implement a Method to Find All Paths
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph:
            return []
        paths = []
        for neighbor in self.graph[start_vertex]:
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, end_vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    # Step 5: Implement a Method to Check if the Graph is Connected
    def is_connected(self):
        if not self.graph:
            return True
        start_vertex = next(iter(self.graph))
        visited = set()
        self._dfs_recursive(start_vertex, visited)
        return len(visited) == len(self.graph)

    # Exercises:
    # 1. Implement a method to find the shortest path between two vertices using BFS.
    def find_shortest_path(self, start, end):
        if start == end:
            return [start]

        queue = deque([[start]])
        visited = set([start])

        while queue:
            path = queue.popleft()
            vertex = path[-1]

            for neighbor in self.graph.get(vertex, []):
                if neighbor == end:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])

        return None  


# Test the Graph class
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()

# Test DFS
print("\nDFS starting from vertex 0:")
g.dfs(0)

# Test BFS
print("\n\nBFS starting from vertex 0:")
g.bfs(0)

# Test finding all paths
print("\n\nAll paths from vertex 0 to vertex 3:")
all_paths = g.find_all_paths(0, 3)
for path in all_paths:
    print(' -> '.join(map(str, path)))

# Test if the graph is connected
print("\nIs the graph connected?", g.is_connected())

# Add a disconnected vertex and test again
g.add_vertex(4)
print("After adding a disconnected vertex:")
print("Is the graph connected?", g.is_connected())

# Test shortest path
print("\nShortest path from vertex 0 to vertex 4:")
shortest_path = g.find_shortest_path(0, 4)
if shortest_path:
    print(" -> ".join(map(str, shortest_path)))
else:
    print("No path found.")

# 2.Add a method to detect cycles in the graph.
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

    # Depth-First Search (DFS)
    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)

    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    # Breadth-First Search (BFS)
    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    # Find All Paths
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph:
            return []
        paths = []
        for neighbor in self.graph[start_vertex]:
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, end_vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    # Check if Graph is Connected
    def is_connected(self):
        if not self.graph:
            return True
        start_vertex = next(iter(self.graph))
        visited = set()
        self._dfs_recursive(start_vertex, visited)
        return len(visited) == len(self.graph)

    # Find Shortest Path Using BFS
    def find_shortest_path(self, start, end):
        if start == end:
            return [start]

        queue = deque([[start]])
        visited = set([start])

        while queue:
            path = queue.popleft()
            vertex = path[-1]

            for neighbor in self.graph.get(vertex, []):
                if neighbor == end:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])

        return None  

    # Cycle Detection for Undirected Graphs
    def has_cycle(self):
        visited = set()

        # Helper function for DFS
        def dfs(vertex, parent):
            visited.add(vertex)

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    if dfs(neighbor, vertex):
                        return True
                elif neighbor != parent:
                    return True
            return False

        # Check for cycles in each connected component
        for vertex in self.graph:
            if vertex not in visited:
                if dfs(vertex, None):
                    return True
        return False


# Testing the cycle detection method
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()

# Test if the graph has a cycle
print("\nDoes the graph contain a cycle?", g.has_cycle())

# 3.Implement Dijkstra's algorithm to find the shortest path in a weighted graph.
import heapq

class WeightedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_weighted_edge(self, node1, node2, cost):
        self.add_node(node1)
        self.add_node(node2)
        self.adj_list[node1].append((node2, cost))
        self.adj_list[node2].append((node1, cost))  # For an undirected graph

    def display_graph(self):
        for node, edges in self.adj_list.items():
            print(f"{node}: {edges}")

    def dijkstra_distances(self, source_node):
        # Initialize distances and previous nodes
        distances = {node: float('inf') for node in self.adj_list}
        distances[source_node] = 0
        predecessors = {node: None for node in self.adj_list}
        priority_queue = [(0, source_node)]
        
        while priority_queue:
            current_cost, current_node = heapq.heappop(priority_queue)

            if current_cost > distances[current_node]:
                continue

            for neighbor, edge_cost in self.adj_list[current_node]:
                alternative_route = current_cost + edge_cost

                if alternative_route < distances[neighbor]:
                    distances[neighbor] = alternative_route
                    predecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (alternative_route, neighbor))

        return distances, predecessors

    def get_shortest_path(self, source_node, destination_node):
        distances, predecessors = self.dijkstra_distances(source_node)

        # Check if there is a path to the destination node
        if distances[destination_node] == float('inf'):
            return None  

        path = []
        current = destination_node
        while current is not None:
            path.insert(0, current)
            current = predecessors[current]

        return path


# Example Usage
graph = WeightedGraph()
graph.add_weighted_edge('A', 'B', 1)
graph.add_weighted_edge('A', 'C', 4)
graph.add_weighted_edge('B', 'C', 2)
graph.add_weighted_edge('B', 'D', 5)
graph.add_weighted_edge('C', 'D', 1)
graph.add_weighted_edge('D', 'E', 3)

print("Graph representation:")
graph.display_graph()

# Find shortest distances from 'A' to all other nodes
distances, _ = graph.dijkstra_distances('A')
print("\nShortest distances from A:", distances)

# Get the shortest path from 'A' to 'E'
path = graph.get_shortest_path('A', 'E')
print("\nShortest path from A to E:", path)

# 4. Create a method to determine if the graph is bipartite.
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1) 

    def is_bipartite(self):
        colors = {}

        def dfs(node, current_color):
            # Assign the current node a color
            colors[node] = current_color

            # Visit all adjacent nodes
            for neighbor in self.graph[node]:
                # If neighbor is uncolored, recursively assign opposite color
                if neighbor not in colors:
                    if not dfs(neighbor, 1 - current_color):
                        return False
                # If neighbor has the same color, graph is not bipartite
                elif colors[neighbor] == colors[node]:
                    return False
            return True

        # Check each component in case the graph is disconnected
        for vertex in self.graph:
            if vertex not in colors:  # Begin DFS if the vertex hasn't been visited yet.
                if not dfs(vertex, 0):  
                    return False
        return True

# Example usage
g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 1)
g.add_edge(1, 3) 

print("Is the graph bipartite?", g.is_bipartite())
