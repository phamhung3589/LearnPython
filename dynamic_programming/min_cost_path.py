# Problem: given a cost matrix cost[row][col] and a position (m, n) ( m < row and n < col)
# Question: find minimum cost path from (0, 0) to (m, n)

# Using recursive approach to returns cost of minimum cost path from (0,0) to (m, n) in mat[R][C]
def min_path_recursive(graph, m, n):

    if m < 0 or n < 0:
        return float("inf")

    if m == 0 and n == 0:
        return graph[0][0]

    return graph[m][n] + min(min_path_recursive(graph, m-1, n),
                             min_path_recursive(graph, m, n-1),
                             min_path_recursive(graph, m-1, n-1))


def min_path_dp(graph, m, n):
    r, c = len(graph), len(graph[0])

    # Instead of following line, we can use int tc[m+1][n+1] or dynamically allocate memoery to save space.
    # The following line is used to keep te program simple and make it working on all compilers.
    dp = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if i == 0 and j == 0:
                dp[i][j] = graph[i][j]

            # Initialize first row of total cost(tc) array
            if i == 0:
                dp[i][j] = graph[i][j] + dp[i][j-1]

            # Initialize first column of total cost(tc) array
            elif j==0:
                dp[i][j] = graph[i][j] + dp[i-1][j]

            # Construct rest of the dp array
            else:
                dp[i][j] = graph[i][j] + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

            if i == m and j == n:
                return dp[i][j]

    return -1


if __name__ == "__main__":
    graph = [[1, 2, 3],
            [4, 8, 2],
            [1, 5, 3]]
    m, n = (2, 2)
    result_recursive = min_path_recursive(graph, m, n)
    result_dp = min_path_dp(graph, m, n)
    print("The min cost path from (0, 0) to ({:d}, {:d}) using recursive approach is: {:d}".format(m ,n , result_recursive))
    print("The min cost path from (0, 0) to ({:d}, {:d}) using dp approach is: {:d}".format(m ,n , result_dp))
