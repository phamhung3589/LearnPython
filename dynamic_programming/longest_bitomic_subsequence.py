# Dynamic Programming implementation of longest bitonic subsequence problem
"""
lbs() returns the length of the Longest Bitonic Subsequence in arr[] of size n. The function
mainly creates two temporary arrays lis[] and lds[] and returns the maximum lis[i] + lds[i] - 1.

lis[i] ==> Longest Increasing subsequence ending with arr[i]
lds[i] ==> Longest decreasing subsequence starting with arr[i]
"""

def lbs(arr):
    n = len(arr)

    # allocate memory for LIS[] and initialize LIS values as 1 for all indexes
    lis = [1 for _ in range(n)]

    # Compute LIS values from left to right
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j] + 1

    # allocate memory for LDS and initialize LDS values for all indexes
    lds = [1 for _ in range(n)]

    # Compute LDS values from right to left
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if arr[i] > arr[j] and lds[j] + 1 > lds[i]:
                lds[i] = lds[j] + 1

    # Return the maximum value of (lis[i] + lds[i] - 1)
    result = 0
    for i in range(n):
        result = max(result, lis[i] + lds[i] - 1)

    return result


if __name__ == "__main__":
    arr = [0 , 8 , 4, 12, 2, 10 , 6 , 14 , 1 , 9 , 5 , 13, 3, 11 , 7 , 15]
    result = lbs(arr)
    print("the longest bitonic subsequence is: ", result)