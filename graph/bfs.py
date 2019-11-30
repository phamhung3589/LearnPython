from collections import defaultdict
# This class represents a directed graph using adjacency list representation
class BFS:

    # Constructor
    def __init__(self, num_vertex):
        self.v = num_vertex
        self.adj = [[] for _ in range(self.v)]

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.adj[u].append(v)

    # Function to print a BFS of graph
    def bfs_run(self):
        # Mark all the vertices as not visited
        visited = [False for _ in range(self.v)]

        # Create a queue for BFS
        queue = []

        # Iterator all vertex
        for i in range(self.v):
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                while len(queue) != 0:
                    # Dequeue a vertex from queue and print it
                    u = queue.pop(0)
                    print(u)

                    # Get all adjacent vertices of the dequeued vertex s. If a adjacent has not been visited,
                    # then mark it visited and enqueue it
                    for v in self.adj[u]:
                        if visited[v] == False:
                            queue.append(v)
                            visited[v] = True

if __name__ == "__main__":
    graph = BFS(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)
    print("the following is Breadth First Search: ")
    graph.bfs_run()
