
def find_k_quick_sort(arr, l, r, k):
    # l == r because this is exactly the kth element - different with quick sort
    if l <= r:

        # Partition the array around last element and get position of pivot element in sorted array
        m = partition(arr, l, r)

        # If position is same as k
        if m == k-1:
            return arr[m]

        # If position is more, recur for left subarray
        if m > k-1:
            return find_k_quick_sort(arr, l, m-1, k)

        # Else recur for right subarray
        return find_k_quick_sort(arr, m+1, r, k)

    # If k is more than number of elements in array
    return -1


# Standard partition process of QuickSort(). It considers the last element as pivot and moves all smaller element
# to left of it and greater elements to right
def partition(arr, l, r):
    pivot = arr[r]
    index = l-1
    for i in range(l, r):
        if arr[i] <= pivot:
            index += 1
            arr[index], arr[i] = arr[i], arr[index]

    arr[index+1], arr[r] = arr[r], arr[index+1]

    return index+1


if __name__ == "__main__":
    arr = [4, 3, 2, 10, 12, 1, 5, 6, 1, 4, 20, 15, 14, 17, 19, 18]
    k = 9
    result = find_k_quick_sort(arr, 0, len(arr)-1, k)
    print("the {:d}th smallest element in arr is: {:d}".format(k, result))