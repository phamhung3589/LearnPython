# l is for left index and r is right index of sub-array of arr to be sorted
def merge_sort(arr, l, r):
    if l < r:
        # middle element
        m = (l+r)//2

        # Sort first and second halves
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)


# Merges two subarrays of arr[]. First subarray is arr[l..m] Second subarray is arr[m+1..r]
def merge(arr, l, m, r):
    # create temp arrays
    arr_1 = arr[l:m+1]
    arr_2 = arr[m+1:r+1]
    len_1 = len(arr_1)
    len_2 = len(arr_2)

    # Index for loop over all element in array_1 and array_2
    i, j = 0, 0
    new_arr = []

    # Loop over each element in arr_1 and arr_2
    while i < len_1 and j < len_2:
        if arr_1[i] < arr_2[j]:
            new_arr.append(arr_1[i])
            i += 1
        else:
            new_arr.append(arr_2[j])
            j += 1

    # Add remain element in array 1 and 2.
    if i < len_1:
        new_arr = new_arr + arr_1[i:]

    if j < len_2:
        new_arr = new_arr + arr_2[j:]

    # Copy all element back to arr
    arr[l:m+1] = new_arr[:len_1]
    arr[m+1:r+1] = new_arr[len_1:]


if __name__ == "__main__":
    arr = [4, 3, 2, 10, 12, 1, 5, 6, 20, 15, 14, 17, 19, 18]

    print("the array before sorting: \n", arr)
    merge_sort(arr, 0, len(arr)-1)
    print("the array after sorting: \n", arr)
