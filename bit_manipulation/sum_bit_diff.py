# Python program to compute sum of pairwise bit differences
def sum_bit_differences(arr):
    n = len(arr)
    # Initialize result
    result = 0
    # traverse over all bits
    for i in range(32):
        # count number of elements with i'th bit set
        count = 0

        for j in range(n):
            if arr[j] & (1 << i):
                count += 1
        # Add "count * (n - count) * 2" to the answer
        result += count * (n - count) * 2

    return result


if __name__ == "__main__":
    arr = [1, 3, 5]
    sum_bit_diff = sum_bit_differences(arr)
    print(" The sum of all pairwise bit differences is: ", sum_bit_diff)