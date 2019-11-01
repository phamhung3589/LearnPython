#  Find the longest chain which can be formed from a given set of pairs. Ex: (a,b), (c,d) => a<b<c<d
def max_length_chain(arr):
    # Sorting the array with the first element
    arr = sorted(arr, key=lambda x: x[0])

    n = len(arr)

    # Initialize dp values for all indices. # dp[i] now stores the maximum chain length ending with pair i
    dp = [1 for _ in range(n)]

    # Compute optimized chain length values in bottom up manner
    for i in range(1, n):
        for j in range(i):
            if arr[j][1] < arr[i][0] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1

    # Pick maximum of all dp values
    return max(dp)


if __name__ == "__main__":
    arr = [[5, 24], [39, 60], [15, 28], [27, 40], [50, 90]]

    result = max_length_chain(arr)
    print("the maximal length chain of pairs is: ", result)
