from collections import defaultdict

# This class represents a directed graph using adjacency list representation
class DFS:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.adj = defaultdict(list)

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.adj[u].append(v)

    # The function to do DFS traversal. It uses recursive DFSUtil()
    def dfs_run(self, u):
        # Mark all the vertices as not visited
        visited = [False for _ in range(len(self.adj))]

        # Call the recursive helper function to print DFS traversal
        self.dfs_util(u, visited)

    # A function used by DFS
    def dfs_util(self, v, visited):

        # Mark the current node as visited and print it
        visited[v] = True
        print(v)

        # Recur for all the vertices adjacent to this vertex
        for i in self.adj[v]:
            if visited[i] == False:
                self.dfs_util(i, visited)

if __name__ == "__main__":
    graph = DFS()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)
    print("Following is DFS from (starting from vertex 2)")
    graph.dfs_run(2)