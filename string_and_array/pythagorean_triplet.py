# Returns true if there is Pythagorean triplet in ar[0..n-1]
def pythagore_triplet(arr):
    n = len(arr)
    # Square all the elemennts
    for i in range(n):
        arr[i] *= arr[i]

    # sort array elements
    arr = sorted(arr)

    # fix one element and find other two i goes from n - 1 to 2
    for i in range(n-1, 1, -1):
        # start two index variables from two corners of the array and move them toward each other
        j, k = 0, i-1

        while j < k:
            # A triplet found
            if arr[j] + arr[k] == arr[i]:
                return True

            elif arr[j] + arr[k] > arr[i]:
                k -= 1

            else:
                j += 1

    # If we reach here, no triplet found
    return False


if __name__ == "__main__":
    arr = [3, 1, 4, 6, 7]

    check = pythagore_triplet(arr)
    print("The pythagorean triplet in arr is: ", check)
