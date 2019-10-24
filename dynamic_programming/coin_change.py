# Recursive Python3 program for coin change problem.
def coin_change_recursive(arr, n, money):
    # If n is 0 then there is 1 solution (do not include any coin)
    if money == 0:
        return 1

    # If n == 0 then no solution exists
    if n == 0:
        return 0

    # If arr[n-1] > money then remove the last coin from array and recursive
    if arr[n-1] > money:
        return coin_change_recursive(arr, n-1, money)

    # Count is sum of solution:
    # (1): including arr[m-1]
    # (2): excluding arr[m-1]
    return coin_change_recursive(arr, n, money-arr[n-1]) + coin_change_recursive(arr, n-1, money)

# using dynamic programming approach for 2-dimensional dp
def coin_change_dp(arr, n, money):
    # building dp table for saving values
    dp = [[0 for _ in range(money+1)] for _ in range(n+1)]

    # Base case: with money = 0, always have 1 ways to choose
    for i in range(n+1):
        dp[i][0] = 1

    # Building from bottom up
    for i in range(1, n+1):
        for j in range(1, money+1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-arr[i-1]]

    return dp[n][money]

# Dynamic Programming Python implementation of Coin Change problem
def coin_change_dp_optimize(arr, money):
    # dp[i] will be storing the number of solutions for value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0) Initialize all dp values as 0
    dp = [0 for _ in range(money+1)]

    # Base case (If given value is 0)
    dp[0] = 1

    # Pick all coins one by one and update the table[] values after the index greater than or equal to the value of the
    # picked coin
    for i in arr:
        for j in range(i, money+1):
            dp[j] = dp[j] + dp[j-i]

    return dp[money]

if __name__ == "__main__":
    arr = [1, 2, 3]
    n = len(arr)
    money = 5
    ways = coin_change_recursive(arr, n, money)
    # ways = coin_change_dp(arr, n, money)
    # ways = coin_change_dp_optimize(arr, money)
    print("number of way to change coin for money =", money, "is:", ways)