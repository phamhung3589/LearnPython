# Naive solution - using recursive to solve this problem
def dice_sum_recursive(m, n, x):
    # Base case - return 0 if number of dice = 0 and sum is still != 0
    if n == 0 and x != 0:
        return 0

    # Base case - return 1 if number of dice = 0 and sum = 0
    elif n == 0 and x == 0:
        return 1

    # set result value
    sum_dice = 0
    # Count all case with all dice, sum_dice will be increased when n = 0 and x = 0
    for i in range(1, m+1):
        if i <= x:
            sum_dice += dice_sum_recursive(m, n-1, x-i)

    return sum_dice

# Using dynamic programming approach to solve this problem
# The main function that returns number of ways to get sum 'x' with 'n' dice and 'm' with m faces.
# Time complexity: m*n*x
def dice_sum_dp(m, n, x):
    # Create a table to store results of subproblems. One extra row and column are used for
    # simpilicity (Number of dice is directly used as row index and sum is directly used as column index).
    # The entries in 0th row and 0th column are never used.
    dp = [[0 for _ in range(x+1)] for _ in range(n+1)]

    # Base case
    for i in range(1, min(m+1, x+1)):
        dp[1][i] = 1

    # Fill rest of the entries in table using recursive relation
    # i: number of dice, j: sum
    for i in range(2, n+1):
        for j in range(1, x+1):
            for k in range(1, min(m+1, j)):
                dp[i][j] += dp[i-1][j-k]

    return dp[n][x]

if __name__ == "__main__":
    m, n, x = 6, 3, 8
    # sum_dice = dice_sum_recursive(m, n, x)
    sum_dice = dice_sum_dp(m, n, x)
    print("the number of ways that sum of n dice = x is:", dice_sum_dp(4, 3, 1))
    print("the number of ways that sum of n dice = x is:", dice_sum_dp(2, 2, 3))
    print("the number of ways that sum of n dice = x is:", dice_sum_dp(6, 3, 8))
    print("the number of ways that sum of n dice = x is:", dice_sum_dp(4, 2, 5))
    print("the number of ways that sum of n dice = x is:", dice_sum_dp(4, 3, 5))