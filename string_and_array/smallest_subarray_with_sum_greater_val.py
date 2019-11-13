# Problem: # Python3 program to find Smallest subarray with sum greater than a given value

# Returns length of smallest subarray with sum greater than x. If there is no subarray with given sum, then returns n+1
def smallest_subarray(arr, x):
    n = len(arr)
    # Check if max(arr) > x or not
    if max(arr) > x:
        return 1

    # Running index to check all subset[j:k+1]
    j, k = 0, 1
    # Initial value for result
    res = float("inf")

    # Loop over k < n
    while k < n:
        # if subarray only have 2 element and sum > x => return 2
        if k-j == 1 and (sum(arr[j:k+1]) > x):
            return 2

        # If sub array > x increase j by 1 and check the smaller sub-array
        elif sum(arr[j:k+1]) > x:
            res = min(res, k-j+1)
            j += 1

        # if sum from j to k <= x, the increase k by 1
        elif sum(arr[j:k+1]) <= x:
            k += 1

    return res


if __name__ == "__main__":
    arr1 = [1, 4, 45, 6, 10, 19]
    x1 = 51
    result = smallest_subarray(arr1, x1)
    print("The snallest sub-array with sum smaller than x has length = ", result)

    arr2 = [1, 10, 5, 2, 7]
    x2 = 9
    result = smallest_subarray(arr2, x2)
    print("The snallest sub-array with sum smaller than x has length = ", result)

    arr3 = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
    x3 = 280
    result = smallest_subarray(arr3, x3)
    print("The snallest sub-array with sum smaller than x has length = ", result)
