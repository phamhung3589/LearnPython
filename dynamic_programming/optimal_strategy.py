# Problem: array of coins: [v1, v2, ..., vn] n is even. you choose 1 coin first at the head or tail of array
#          opponent choose the next turn.
#          Determine the maximum possible amount of money if you play first

# Recursive approach:
# if you choose coin vi(from first) - opponent choose coin for minimum your values - it can v(i+1) or v(j)
#        => your values: vi + min(optimal(arr, i+1, j-1), optimal(arr, i+2, j))
# if you choose coin vj (from head) - opponent choose coin for minimum values - it can be vj-1 or vi
#        => your values: vj + min(optimal(arr, i+1, j-1), optimal(arr, i, j-2))
def optimal_strategy_recursive(arr, m, n):
    if n-m==1:
        return max(arr[m], arr[n])

    if m == n:
        return arr[m]

    return max(arr[m] + min(optimal_strategy_recursive(arr, m+1, n-1), optimal_strategy_recursive(arr, m+2, n)),
               arr[n] + min(optimal_strategy_recursive(arr, m+1, n-1), optimal_strategy_recursive(arr, m, n-2)))


# Using dp approach
def optimal_strategy_dp(arr):
    n = len(arr)
    # table[n][n] for optimmize values if you play first, dp[i][j] is max values with index from i to j
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Base case, if arr only 1 value, you values is the value of this element
    for i in range(n):
        dp[i][i] = arr[i]

    # loop through element in n
    for i in range(n):

        # j run from i-1 to 0
        for j in range(i-1, -1, -1):

            # If array only have 2 element, your value is the max value in array
            if i-j==1:
                dp[j][i] = max(arr[j], arr[i])
            else:
                # The main case corresponding to recursive approach
                dp[j][i] = max(arr[j] + min(dp[j+1][i-1], dp[j+2][i]),
                               arr[i] + min(dp[j+1][i-1], dp[j][i-2]))

    return dp[0][n-1]


if __name__ == "__main__":
    arr = [20, 30, 2, 2, 2, 10]
    result_recursive = optimal_strategy_recursive(arr, 0, len(arr)-1)
    result_dp = optimal_strategy_dp(arr)

    print("The optimal point of first player is: ", result_recursive)
    print("The optimal point of first player is: ", result_dp)
