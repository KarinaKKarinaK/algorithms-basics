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
        self.graph[u].append(v)

    def bfs(self, root):
        visited = set() # Create a visited array using the set() function
        queue = collections.deque([root])

        while queue: # While queue is not empty
            vertex = queue.popleft() # dequeues teh element rom teh left part and stores it as a vertex variable
            visited.add(vertex) #Adding teh vertex to teh array of visited nodes

            # Now you have to push all teh adjacent nodes (adjacent to teh node you just visited) to the queue (enqueue) 
            # - on teh condition that they have not yet been visited

            for i in self.graph[vertex]:
                if i not in visited:
                    queue.append(i)
        return visited
    
    # DFS ============================================================================================================
    # Depth First Search (DFS) is a fundamental graph traversal algorithm. It begins with a
    # node, then explores as far as possible along each branch before backtracking.
    # DFS is different from BFS in a way that it goes deep into the graph whenever possible.
    # Popular graph algorithms like Topological Sort, Strongly Connected Components, and solving puzzles like
    # mazes are based on DFS. DFS itself can be used to detect cycle in a directed and undirected graph, find connected components in a graph and many more problems.   

    def dfs(self, root):
        visited = set()
        stack = [root]

        while stack:
            node = stack.pop

            if node not in visited:
                visited.add(node)
                print(node)
                stack.extend(reversed(self.graph[root]))




# Example graph as adjacency list (nodes are numbers)
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [6],
    6: []
}

# Test DFS
print("DFS traversal starting from 1:")
print(dfs(graph, 1))

# Test BFS
print("BFS traversal starting from 1:")
print(bfs(graph, 1))