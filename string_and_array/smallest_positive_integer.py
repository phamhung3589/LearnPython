# find the smallest positive value that cannot be represented as sum of subsets of a given sorted array

# Returns the smallest number that cannot be represented as sum of subset of elements from set represented
# by sorted array arr[0..n-1]
def smallest_integer(arr):
    # Initialize result
    res = 1

    # Traverse the array and increment 'res' if arr[i] is smaller than or equal to 'res'.
    # if arr[i] > res, return res because all element from 0 to i-1 can represented from 1 - res-1,
    # all elements from i > res => res is the gap value
    # if arr[i] <= res, increase res += arr[i], because all elements from 0=>i-1 can represented from 1-res.
    for i in range(len(arr)):
        if arr[i] <= res:
            res += arr[i]
        else:
            break

    return res


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    result = smallest_integer(arr)
    print("The smallest element that cannot be represented as sum of any subset in arr is: ", result)

    arr1 = [1, 3, 4, 5]
    result = smallest_integer(arr1)
    print("The smallest element that cannot be represented as sum of any subset in arr is: ", result)

    arr2 = [1, 2, 6, 10, 11, 15]
    result = smallest_integer(arr2)
    print("The smallest element that cannot be represented as sum of any subset in arr is: ", result)

    arr3 = [1, 1, 1, 1]
    result = smallest_integer(arr3)
    print("The smallest element that cannot be represented as sum of any subset in arr is: ", result)
