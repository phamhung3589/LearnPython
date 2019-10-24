
global maximum
def lis_recursive(arr, n):
    global maximum
    if n == 1:
        return 1

    maxEnding = 1

    for i in range(1, n):
        result = lis_recursive(arr, i)
        if arr[i-1] < arr[n-1] and result + 1 > maxEnding:
            maxEnding = result + 1

    maximum = max(maximum, maxEnding)

    return maxEnding

if __name__== "__main__":
    global maximum
    maximum = 1
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    result = lis_recursive(arr, len(arr))
    print(result)
