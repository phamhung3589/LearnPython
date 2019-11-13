# Problem: Given an array of distinct integers, find length of the longest subarray which contains numbers that can be
# arranged in a continuous sequence.

def largest_subarray_sort(arr):
    n = len(arr)

    # Sort array
    arr = sorted(arr)

    # Using dp to store each length of the longest subarray
    dp = [1 for _ in range(n)]

    for i in range(1, n):
        # if arr[i] and arr[i-1] is contigous => dp[i] = dp[i-1] + 1
        if arr[i] - arr[i-1] == 1:
            dp[i] = dp[i-1] + 1

    # Return max length of all sub-array
    return max(dp)


# save min and max element in each sub array, if max - min = length of subarray => it can be arranged to contiguous ele
def largest_subarray(arr):
    n = len(arr)
    # Initialize result
    max_len = 0

    for i in range(n-1):

        # Initialize min and max for all subarrays starting with i
        max_tmp = arr[i]
        min_tmp = arr[i]

        # Consider all subarrays starting with i and ending with j
        for j in range(i+1, n):
            # Update min and max in this subarray if needed
            max_tmp = max(max_tmp, arr[j])
            min_tmp = min(min_tmp, arr[j])

            # If current subarray has all contiguous elements
            if max_tmp - min_tmp == j - i:
                max_len = max(max_len, max_tmp - min_tmp + 1)

    return max_len


if __name__ == "__main__":
    arr = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
    result_sort = largest_subarray_sort(arr)
    result = largest_subarray(arr)

    print("The largest subaaray that can be arranged to contiguous elements using sorting is: ", result_sort)
    print("The largest subaaray that can be arranged to contiguous elements without using sorting is: ", result)
