# search element in rotated ascending order sorted array at some pivot unknown to you beforehand.
# So for instance, 1 2 3 4 5 might become 3 4 5 1 2

# Approach: find pivot that rotate and divide the array into 2 subset. find bin search for each subset - O(log n)
def search_rotated_array(arr, key):
    l = 0
    r = len(arr)-1
    compare = arr[0]

    while r - l > 1:
        m = (r+l)//2

        if arr[m] > compare:
            l = m

        else:
            r = m
            compare = arr[m]

    # Check element in first subset
    index_1 = bin_search(arr[:r], 0, r-1, key)
    if index_1 != -1:
        return index_1

    # if not exist in first subset, Find element in the second subset
    return r + bin_search(arr[r:], 0, len(arr[r:]), key)


# Binary search of sorted array
def bin_search(arr, l, r, key):

    while l < r:
        m = (l+r)//2

        if arr[m] == key:
            return m

        if arr[m] > key:
            r = m-1

        else:
            l = m+1

    return -1


if __name__ == "__main__":
    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key = 3
    index = search_rotated_array(arr, key)
    print("index of element {:d} in arr is: {:d}".format(key, index))
