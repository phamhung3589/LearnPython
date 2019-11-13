# Python3 program to count triplets with sum smaller than a given value

# Function to count triplets with sum smaller than a given value
def count_triplet(arr, s):
    n = len(arr)
    # Sort input array
    arr = sorted(arr)

    # Initialize result
    result = 0

    # Every iteration of loop counts triplet with first element as arr[i].
    for i in range(n-2):

        # Initialize other two elements as corner elements of subarray arr[j+1..k]
        j, k = i+1, n-1
        remain = s - arr[i]

        # # Use Meet in the Middle concept
        while j < k:

            # If sum of current triplet is more or equal, move right corner to look for smaller values
            if arr[j] + arr[k] >= remain:
                k -= 1

            # Else move left corner
            else:
                # This is important. For current i and j, there can be total k-j third elements.
                result += k-j
                j += 1

    return result


if __name__ == "__main__":
    arr = [5, 1, 3, 4, 7]
    s = 12
    result = count_triplet(arr, s)
    print("the number of triplet with sum smaller than {:d} is: {:d}".format(s, result))
