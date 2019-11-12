def heap_sort(arr):
    n = len(arr)

    for i in range(n-1, -1, -1):
        # max heapyfy at the root node
        heapyfy(arr, i)
        # Assign max value to the tail of the array
        arr[i], arr[0] = arr[0], arr[i]


def heapyfy(arr, n):
    # Get the max node have child in heapyfy
    index = (n-1)//2

    # Loop from the last node has child to the first node
    for i in range(index, -1, -1):
        # with parent i, the node left is: 2*i+1, node right is 2*i+2
        left = i*2+1
        right = i*2+2

        # Change node parent with left node
        if left <= n and arr[i] < arr[left]:
            arr[i], arr[left] = arr[left], arr[i]

        # Change node parent with right node
        if right <= n and arr[i] < arr[right]:
            arr[i], arr[right] = arr[right], arr[i]


if __name__ == "__main__":
    arr = [4, 3, 2, 10, 12, 1, 5, 6, 1, 4, 20, 15, 14, 17, 19, 18]

    print("the array before sorting: \n", arr)
    heap_sort(arr)
    print("the array after sorting: \n", arr)