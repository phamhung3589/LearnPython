# global variable to store the maximum
global maximum
# Using recursive approach
def lis_recursive(arr, n):
    # to allow the access of global variable
    global maximum

    # Base case
    if n == 1:
        return 1

    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere = 1

    # Recursively get all LIS ending with arr[0], arr[1]..arr[n-2] IF arr[n-1] is maller than arr[n-1],
    # and max ending with arr[n-1] needs to be updated, then update it
    for i in range(1, n):
        result = lis_recursive(arr, i)
        if arr[i-1] < arr[n-1] and result + 1 > maxEndingHere:
            maxEndingHere = result + 1

    # Compare maxEndingHere with overall maximum. And update the overall maximum if needed
    maximum = max(maximum, maxEndingHere)

    return maxEndingHere

# Using dynamic programming approach - O(n^2)
def lis_dp(arr):
    n = len(arr)

    # Initialize LIS values for all indexes
    lis = [1]*n

    # compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j] + 1

    # Return the maximum values in LIS array
    return max(lis)

# Using Optimize approach - O(nlogn)
def lis_optimize(arr):
    n = len(arr)

    # Add boundary case, when array size is one
    l = [0]*(n+1)
    l[0] = arr[0]
    length = 1
    for i in range(1, n):
        if arr[i] < l[0]:
            # new smallest value
            l[0] = arr[i]

        elif arr[i] > l[length-1]:
            # l[i] wants to extend largest sub-sequence
            l[length] = arr[i]
            length += 1

        else:
            # l[i] wants to be current end candidate of an existing subsequence. It will replace
            # ceil value in tailTable
            index = binSearch(l, -1, length-1, arr[i])
            l[index] = arr[i]

    return length

# Binary search (note boundaries in the caller) A[] is ceilIndex in the caller
def binSearch(A, l, r, key):
    while r-l>1:
        m = (r+l)//2
        if A[m] >= key:
            r = m
        else:
            l = m
    print(A, key, r)
    return r

if __name__ == "__main__":
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    global maximum
    maximum = 1
    # result = lis_recursive(arr, len(arr))
    # result = lis_dp(arr)
    result = lis_optimize(arr)
    print(result)