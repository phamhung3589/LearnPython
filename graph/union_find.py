from collections import defaultdict


# Python Program for union-find algorithm to detect cycle in a undirected graph
# we have one egde for any two vertex i.e 1-2 is either 1-2 or 2-1 but not both
class Graph(object):

    def __init__(self, vertices):
        # No. of vertices
        self.v = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def add_edge(self, a, b):
        self.graph[a].append(b)

    # A utility function to find the subset of an element i
    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i

        return self.find_parent(parent, parent[i])

    # A utility function to do union of two subsets
    def union(self, parent, x, y):
        a = self.find_parent(parent, x)
        b = self.find_parent(parent, y)
        parent[a] = b

    # The main function to check whether a given graph contains cycle or not
    def is_cycle(self):
        # Allocate memory for creating V subsets and Initialize all subsets as single element sets
        parent = [-1 for _ in range(self.v)]

        # Iterate through all edges of graph, find subset of both vertices of every edge, if both subsets are same, then
        # there is cycle in graph
        for i in self.graph:
            for j in self.graph[i]:
                a = self.find_parent(parent, i)
                b = self.find_parent(parent, j)
                if a == b:
                    print(parent)
                    return True
                self.union(parent, a, b)

        return False


if __name__ == "__main__":
    # Create a graph given in the above diagram
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(5, 1)

    if g.is_cycle():
        print("graph contain cycle")
    else:
        print("Graph does not contain cycle")
