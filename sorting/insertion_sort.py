def insertion(arr):
    n = len(arr)

    for i in range(1, n):
        tmp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > tmp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = tmp


if __name__ == "__main__":
    arr = [4, 3, 2, 10, 12, 1, 5, 6]

    print("the array before sorting: \n", arr)
    insertion(arr)
    print("the array after sorting: \n", arr)
