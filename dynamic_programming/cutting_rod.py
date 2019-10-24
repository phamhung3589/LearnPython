# A naive recursive solution for rod cutting problem
def cutting_recursive(price, rod_size):
    max_size = 0
    if rod_size <= 0:
        return 0

    # Recursively cut the rod in different pieces and compare different configurations
    for i in range(rod_size):
        max_size = max(max_size, price[i] + cutting_recursive(price, rod_size-i-1))

    return max_size

# Using dynamic programming approach
def cutting_dp(price, rod_size):
    dp = [0 for _ in range(rod_size+1)]

    # Build the table val[] in bottom up manner and return the last entry from the table
    for i in range(1, rod_size+1):
        max_value = 0
        for j in range(i):
            max_value = max(max_value, price[j] + dp[i-j-1])
        dp[i] = max_value

    return dp[rod_size]

if __name__ == "__main__":
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    rod = len(price)
    print("maximum obtainable value is: ", cutting_dp(price, rod))