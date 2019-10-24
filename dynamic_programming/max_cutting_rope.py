# Naive solution using recursive
def max_production_recursive(n):
    # Base case
    if n == 0: return 1
    max_rope = 0
    # Make a cut at different places and take the maximum of all
    for i in range(1, n+1):
        max_rope = max(max_rope, i * max_production_recursive(n-i))

    # Return the maximum of all values
    return max_rope

# Dynamic solution
def max_production_dp(n):

    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    # Build the table dp[] in bottom up manner and return the last entry from the table
    for i in range(2, n+1):
        max_rope = 0
        for j in range(1, i+1):
            max_rope = max(max_rope, j * dp[i-j])
        dp[i] = max_rope
    return dp[n]

if __name__ == "__main__":
    n = 10
    # max_rope = max_production_recursive(n)
    max_rope = max_production_dp(n)
    print("max product of cutting the rope with length = {:d} is {:d}".format(n, max_rope))