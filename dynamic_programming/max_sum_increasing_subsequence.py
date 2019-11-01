from copy import copy

global max_result


def max_increasing_sum_dp(arr):
    n = len(arr)
    dp = copy(arr)

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + arr[i] > dp[i]:
                dp[i] = dp[j] + arr[i]

    return max(dp)


if __name__ == "__main__":
    global max_result
    max_result = 0
    arr = [1, 101, 2, 3, 100, 4, 5]
    n = len(arr)
    result_dp = max_increasing_sum_dp(arr)
    print("the maximal sum of increasing subsequence using dp approach is: ", result_dp)
