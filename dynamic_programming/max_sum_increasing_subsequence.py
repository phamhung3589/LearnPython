from copy import copy


# max_increasing_sum_dp() returns the maximum sum of increasing subsequence in arr[] of size n
def max_increasing_sum_dp(arr):
    n = len(arr)
    # Initialize msis values for all indexes
    dp = copy(arr)

    # Compute maximum sum values in bottom up manner
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + arr[i] > dp[i]:
                dp[i] = dp[j] + arr[i]

    # Pick maximum of all msis values
    return max(dp)


if __name__ == "__main__":
    arr = [1, 101, 2, 3, 100, 4, 5]
    n = len(arr)
    result_dp = max_increasing_sum_dp(arr)
    print("the maximal sum of increasing subsequence using dp approach is: ", result_dp)
