# Kruskal's algorithm to find Minimum Spanning Tree of a given connected, undirected and weighted graph
class MST(object):

    def __init__(self, vertices):
        # No. of vertices
        self.v = vertices
        # default array to store graph
        self.graph = []

    # Function to add an edge with cost to graph
    def add_edge(self, a, b, cost):
        self.graph.append([a, b, cost])

    # A utility function to find set of an element i
    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i

        return self.find_parent(parent, parent[i])

    # A function that does union of two sets of x and y
    def union(self, parent, x, y):
        a = self.find_parent(parent, x)
        b = self.find_parent(parent, y)
        parent[a] = b

    # The main function to construct MST using Kruskal's algorithm
    def kruskal(self):
        # Step 1:  Sort all the edges in non-decreasing order of their weight.
        self.graph = sorted(self.graph, key=lambda x: x[2])
        parent = [-1 for _ in range(self.v)]

        # This will store the resultant MST
        mst = []
        edge = 0

        # Number of edges to be taken is equal to V-1
        while edge < self.v-1:
            # Step 2: Pick the smallest edge and increment the index for next iteration
            for a, b, c in self.graph:
                x = self.find_parent(parent, a)
                y = self.find_parent(parent, b)

                # If including this edge does't cause cycle, include it in result and increment the index of result
                # for next edge
                if x != y:
                    self.union(parent, x, y)
                    edge += 1
                    mst.append([a, b, c])

        # print the contents of mst[] to display the built MST
        for a, b, c in mst:
            print("{:d} --> {:d} == {:d}".format(a, b, c))


if __name__ == "__main__":
    mst = MST(9)
    mst.add_edge(0, 1, 4)
    mst.add_edge(0, 7, 8)
    mst.add_edge(1, 2, 8)
    mst.add_edge(1, 7, 11)
    mst.add_edge(2, 8, 2)
    mst.add_edge(2, 3, 7)
    mst.add_edge(2, 5, 4)
    mst.add_edge(3, 5, 14)
    mst.add_edge(3, 4, 9)
    mst.add_edge(4, 5, 10)
    mst.add_edge(5, 6, 2)
    mst.add_edge(6, 8, 6)
    mst.add_edge(6, 7, 1)
    mst.add_edge(7, 8, 7)
    mst.kruskal()
