# Naive approach using recursive
def egg_dropping(egg, floor):
    # If there are no floors, then no trials needed. OR if there is one floor, one trial needed.
    if floor == 0 or floor == 1:
        return floor

    # We need k trials for one egg and k floors
    if egg == 1:
        return floor

    min_drop = float("inf")

    # Consider all droppings from 1st floor to kth floor and return the minimum of these values plus 1.
    for i in range(1, floor+1):
        result = max(egg_dropping(egg-1, i-1), egg_dropping(egg, floor-i))
        min_drop = min(min_drop, result)

    return min_drop+1

# A Dynamic Programming based Python Program for the Egg Dropping Puzzle
def egg_dropping_dp(egg, floor):
    # A 2D table where enter dp[i][j] will represent minimum number of trials needed for i eggs and j floors.
    dp = [[0 for _ in range(floor+1)] for _ in range(egg+1)]

    # We always need j trials for one egg and j floors.
    for i in range(1, floor+1):
        dp[1][i] = i

    # We need one trial for one floor and 0 trials for 0 floors
    for i in range(1, egg+1):
        dp[i][1] = 1

    # Fill rest of the entries in table using optimal substructure property
    for i in range(2, egg+1):
        for j in range(2, floor+1):
            dp[i][j] = float("inf")
            for x in range(1, j+1):
                result = 1 + max(dp[i-1][x-1], dp[i][j-x])
                dp[i][j] = min(result, dp[i][j])

    # dp[n][k] holds the result
    return dp[egg][floor]


if __name__ == "__main__":
    egg = 2
    floor = 36
    # min_drop = egg_dropping(egg, floor)
    min_drop = egg_dropping_dp(egg, floor)
    print("Minimum number of trials in worse case with {:d} eggs and {:d} floor is: {:d} ".format(egg, floor, min_drop))

