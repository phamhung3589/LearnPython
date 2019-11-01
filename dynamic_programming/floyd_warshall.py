from copy import copy

#The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph.

# Solves all pair shortest path via Floyd Warshall Algorithm 
def all_pair_shortest_path(graph):
    n = len(graph)

    """ dp will be the output matrix that will finally have the shortest distances between every pair of vertices """
    """ initializing the solution matrix same as input graph matrix OR we can say that the initial values of shortest 
    distances are based on shortest paths considering no intermediate vertices """
    dp = copy(graph)

    """ Add all vertices one by one to the set of intermediate vertices. 
    ---> Before start of an iteration, we have shortest distances between all pairs of vertices such that the shortest 
      distances consider only the vertices in the set {0, 1, 2, .. k-1} as intermediate vertices. 
    ---> After the end of a iteration, vertex no. k is added to the set of intermediate vertices and the  set becomes 
    {0, 1, 2, .. k} """
    for k in range(n):

        # pick all vertices as source one by one
        for i in range(n):

            # Pick all vertices as destination for the above picked source
            for j in range(n):

                # If vertex k is on the shortest path i to j, then update the value of dist[i][j]
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    return dp


if __name__ == "__main__":
    graph = [[0, 5, float("inf"), 10],
             [float("inf"), 0, 3, float("inf")],
             [float("inf"), float("inf"), 0, 1],
             [float("inf"), float("inf"), float("inf"), 0]]
    result = all_pair_shortest_path(graph)
    print(result)
