
def count_num_step(steps):
    dp = [0 for _ in range(steps+1)]
    # Initialize base values. There is one way to cover 0 and 1 distances and two ways to cover 2 distance
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    # Fill the count array in bottom up manner
    for i in range(3, steps+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[steps]

if __name__ == "__main__":
    dist = 4
    print("num steps: ", count_num_step(dist))
