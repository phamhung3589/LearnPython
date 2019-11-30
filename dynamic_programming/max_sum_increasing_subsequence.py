from copy import copy


# max_increasing_sum_dp() returns the maximum sum of increasing subsequence in arr[] of size n
# input = {1, 101, 2, 3, 100, 4, 5} => output = 106 (1 + 2 + 3 + 100),
# input = {3, 4, 5, 10}, => output = 22 (3 + 4 + 5 + 10)
# input = {10, 5, 4, 3}, => output = 10
def max_increasing_sum_dp(arr):
    n = len(arr)
    # Initialize msis values for all indexes
    dp = [1 for _ in range(n)]
    result = 0

    # Compute maximum sum values in bottom up manner
    for i in range(1, n):
        max_tmp = arr[i]
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                max_tmp += arr[j]
        result = max(result, max_tmp)

    # Pick maximum of all msis values
    return result


if __name__ == "__main__":
    arr = [1, 101, 2, 3, 100, 4, 5]
    n = len(arr)
    result_dp = max_increasing_sum_dp(arr)
    print("the maximal sum of increasing subsequence using dp approach is: ", result_dp)
