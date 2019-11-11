def optimal_strategy_recursive(arr, m, n):
    if m > n:
        return float("inf")

    if m == n:
        return arr[m]

    return max(arr[m] + min(optimal_strategy_recursive(arr, m+1, n-1), optimal_strategy_recursive(arr, m+2, n)),
               arr[n] + min(optimal_strategy_recursive(arr, m+1, n-1), optimal_strategy_recursive(arr, m, n-2)))


def optimal_strategy_dp(arr):
    n = len(arr)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = arr[i]

    for i in range(n):
        for j in range(i-1, -1, -1):
            if i-j==1:
                dp[j][i] = max(arr[j] + dp[j+1][i], arr[i] + dp[j][i-1])
            else:
                dp[j][i] = max(arr[j] + min(dp[j+1][i-1], dp[j+2][i]),
                               arr[i] + min(dp[j+1][i-1], dp[j][i-2]))

    return dp[0][n-1]


if __name__ == "__main__":
    arr = [8, 15, 3, 7]
    result_recursive = optimal_strategy_recursive(arr, 0, len(arr)-1)
    result_dp = optimal_strategy_dp(arr)

    print("The optimal point of first player is: ", result_recursive)
    print("The optimal point of first player is: ", result_dp)