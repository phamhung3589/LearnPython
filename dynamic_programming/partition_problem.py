# A utility function that returns true if there is a subset of arr[] with sun equal to given sum
def is_partition(arr, sum, n):
    # base case
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

    # is last element is greater than sum, then ignore it
    if arr[n-1] > sum:
        return is_partition(arr, sum, n-1)

    # Else, check if sum can be obtained by any of the following:
    # (1): including the last element
    # (2): excluding the last element
    return is_partition(arr, sum, n-1) or is_partition(arr, sum-arr[n-1], n-1)

# Using dynamic programming approach
def is_partition_dp(arr, sum, n):

    dp = [[True for _ in range(sum+1)] for _ in range(n+1)]
    # Initialize top row is False, (corresponding to using 0 element with sum equal 1 - sum)
    for i in range(1, sum+1):
        dp[0][i] = False

    # Fill the partition table in bottom up manner
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]

    return dp[n][sum]

if __name__ == "__main__":
    arr = [1, 5, 11, 5]
    sum_arr = sum(arr)
    check = False
    # If sum is odd, there cannot be two subsets with equal sum
    if sum_arr % 2 == 1:
        print("this array cannot be partitioned into 2 subsets")
    else:
        check = is_partition_dp(arr, sum_arr//2, len(arr))
    print("this array can be partitioned into 2 same subsets:", check)