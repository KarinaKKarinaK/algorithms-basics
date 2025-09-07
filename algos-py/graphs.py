from collections import defaultdict
# BFS and DFS

# BFS ============================================================================================================
# Breadth First Search (BFS) is a fundamental graph traversal algorithm. It begins with a node, then first 
# traverses all its adjacent nodes. Once all adjacent are visited, then their adjacent are traversed.

# BFS is different from DFS in a way that closest vertices are visited before others. We mainly traverse vertices level by level.
# Popular graph algorithms like Dijkstra’s shortest path, Kahn’s Algorithm, and Prim’s algorithm are based on BFS.
# BFS itself can be used to detect cycle in a directed and undirected graph, find shortest path in an unweighted graph and many more problems.

# Follow the below given approach:

# Initialization: Enqueue the given source vertex into a queue and mark it as visited.
# Exploration: While the queue is not empty:
# Dequeue a node from the queue and visit it (e.g., print its value).
# For each unvisited neighbor of the dequeued node:
# Enqueue the neighbor into the queue.
# Mark the neighbor as visited.
# Termination: Repeat step 2 until the queue is empty.

class Graph:
    def __init__(self):
        self.graph = defaultdict(list) # Using the defaultdict to store the graph

    def add_edge(self, u, v):
        self.graph[u].append[v]
    
    def BFS(self, root):
        visited = set() # Create a visited array using the set() function

graph1 = {0:[1, 2, 3], 1:[0, 2], 2:[0,1], 3:[0], 4:[2]}