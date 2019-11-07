# Prim's Minimum Spanning Tree (MST) algorithm. The program is for adjacency matrix representation of the graph
class MST(object):

    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for _ in range(self.v)] for _ in range(self.v)]

    def add_edge(self, a, b, cost):
        self.graph[a][b] = cost
        self.graph[b][a] = cost

    # A utility function to find the vertex with minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def min_vertex(self, dist, visited):
        min_v = float("inf")
        min_i = -1

        for i, v in enumerate(dist):
            if visited[i] == False and v < min_v:
                min_v = v
                min_i = i

        return min_i

    # A utility function to print the constructed MST stored in parent[]
    def print_vertex(self, parent):
        for i, v in enumerate(parent):
            if i != 0:
                print("{:d} --> {:d} == {:d}".format(i, v, self.graph[i][v]))

    # Function to construct and print MST for a graph represented using adjacency matrix representation
    def prim(self):

        visited = [False for _ in range(self.v)]

        # Initial distance for dist arr - Make dist[0] = 0 so that this vertex is picked as first vertex
        dist = [float("inf") for _ in range(self.v)]
        dist[0] = 0
        parent = [None for _ in range(self.v)]

        # First node is always the root of
        parent[0] = -1

        for _ in range(self.v):

            # Pick the minimum distance vertex from the set of vertices not yet processed.
            u = self.min_vertex(dist, visited)

            # Put the minimum distance vertex in the shortest path tree
            visited[u] = True

            # Update dist value of the adjacent vertices of the picked vertex only if the current distance is greater
            # than new distance and the vertex in not in the shotest path tree
            for v in range(self.v):
                # graph[u][v] is non zero only for adjacent vertices of m visited[v] is false for vertices not yet
                # included in MST Update the key only if graph[u][v] is smaller than dist[v]
                if self.graph[u][v] > 0 and visited[v] == False and dist[v] > self.graph[u][v]:
                    dist[v] = self.graph[u][v]
                    parent[v] = u

        self.print_vertex(parent)


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
    mst.prim()
