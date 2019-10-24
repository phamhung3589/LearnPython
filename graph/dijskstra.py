# A utility function to find the vertex with minimum distance value, from the set of vertices
# not yet included in shortest path tree
def get_min_dist(dist, visited):

    # Initilaize minimum distance for next node
    min_dist = float("inf")
    index = -1

    # Search not nearest vertex not in the shortest path tree
    for i, v in enumerate(dist):
        if visited[i] == False and v != float("inf") and v < min_dist:
            min_dist = v
            index = i

    return index

# Funtion that implements Dijkstra's single source shortest path algorithm for a graph represented
# using adjacency matrix representation
def dijsktra(graph, src):
    node = len(graph)
    visited = [False for _ in range(node)]
    dist = [float("inf") for _ in range(node)]
    dist[src] = 0

    for _ in range(node-1):

        # Pick the minimum distance vertex from the set of vertices not yet processed.
        # u is always equal to src in first iteration
        min_vertex = get_min_dist(dist, visited)

        # Put the minimum distance vertex in the shortest path tree
        visited[min_vertex] = True

        # Update dist value of the adjacent vertices of the picked vertex only if the current
        # distance is greater than new distance and the vertex in not in the shotest path tree
        for i, v in enumerate(graph[min_vertex]):
            if v != 0 and visited[i] == False and dist[min_vertex] + v < dist[i]:
                dist[i] = dist[min_vertex] + v

    for i, v in enumerate(dist):
        print(src, "=>", i, "=", v)


if __name__ == "__main__":
    graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    dijsktra(graph, 0)