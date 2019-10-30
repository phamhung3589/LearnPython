# Problem: n items with weights = [], val = []. W = Capacity
# Find the maximum value of k items in n items with sum weights of k items < W

# Using recursive approach
def knapsack_recursive(val, wt, n, W):
    # Base case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if wt[n-1] > W:
        return knapsack_recursive(val, wt, n-1, W)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    return max(val[n-1] + knapsack_recursive(val, wt, n-1, W-wt[n-1]), knapsack_recursive(val, wt, n-1, W))

# Using dynamic programming approach
def knapsack_dp(val, wt, n, W):
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

    # Build table K[][] in bottom up manner
    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1] <= j:
                dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][W]

if __name__ == "__main__":
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    print(knapsack_dp(val, wt, n, W))
