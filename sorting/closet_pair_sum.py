# Python3 program to find the pair with sum closest to a given no.

#Prints the pair with sum closest to x
def sum_closet_pair(arr, s):
    n = len(arr)
    # To store indexes of result pair
    res_l, res_r = 0, 0

    # Initialize left and right indexes and difference between pair sum and x
    l, r, diff = 0, n-1, float("inf")

    # While there are elements between l and r
    while l < r:

        # Check if this pair is closer than the closest pair so far
        if abs(arr[l] + arr[r] - s) < diff:
            res_l, res_r = l, r
            diff = abs(arr[l] + arr[r] - s)

        if arr[l] + arr[r] > s:
            # If this pair has more sum, move to smaller values.
            r -= 1
        else:
            # Move to larger values
            l += 1

    print("the pair with sum closet to {:d} is: {:d}, {:d}".format(s, arr[res_l], arr[res_r]))


if __name__ == "__main__":
    arr = [10, 22, 28, 29, 30, 40]
    s = 54
    sum_closet_pair(arr, s)
