from collections import defaultdict


#Python program to print topological sorting of a DAG
class Graph(object):

    def __init__(self, vertices):
        # No. of vertices
        self.v = vertices
        # dictionary containing adjacency List
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def add_edge(self, a, b):
        self.graph[a].append(b)

    # A recursive function used by topologicalSort
    def topology_util(self, visited, stack, i):
        # Mark the current node as visited.
        visited[i] = True

        # Recur for all the vertices adjacent to this vertex
        for ele in self.graph[i]:
            if visited[ele] is False:
                self.topology_util(visited, stack, ele)

        # Push current vertex to stack which stores result
        stack.insert(0, i)

    # The function to do Topological Sort. It uses recursive topological_util()
    def topology(self):
        # Mark all the vertices as not visited
        visited = [False for _ in range(self.v)]
        stack = []

        # Call the recursive helper function to store Topological Sort starting from all vertices one by one
        for i in range(self.v):
            if visited[i] is False:
                self.topology_util(visited, stack, i)

        # Print contents of the stack
        print(*stack)


if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(5, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    g.add_edge(4, 1)
    print("The topological sort of the given graph")
    g.topology()
