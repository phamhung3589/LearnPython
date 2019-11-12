# This function takes last element as pivot, places the pivot element at its correct position in sorted array,
# and places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot
def partition(arr, l, r):
    # pivot
    pivot = arr[r]
    # index of smaller element
    index = l-1

    for i in range(l, r):

        # If current element is smaller than the pivot
        if arr[i] <= pivot:
            # increment index of smaller element
            index += 1
            arr[index], arr[i] = arr[i], arr[index]

    arr[index+1], arr[r] = arr[r], arr[index+1]

    return index+1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quick_sort(arr, l, r):
    if l < r:
        # m is partitioning index, arr[p] is now at right place
        m = partition(arr, l, r)

        # Separately sort elements before partition and after partition
        quick_sort(arr, l, m-1)
        quick_sort(arr, m+1, r)


if __name__ == "__main__":
    arr = [4, 3, 2, 10, 12, 1, 5, 6, 1, 4, 20, 15, 14, 17, 19, 18]

    print("the array before sorting: \n", arr)
    quick_sort(arr, 0, len(arr)-1)
    print("the array after sorting: \n", arr)
