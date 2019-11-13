# sort an arra yof DISTINCT elements in Zig-Zag form.  The converted array should be in form a < b > c < d > e < f.

def zig_zag_array(arr):
    n = len(arr)

    # Flag true indicates relation "<" is expected, else ">" is expected.  The first expected relation is "<"
    flag = True

    for i in range(n-1):

        # "<" relation expected
        if flag and arr[i] > arr[i+1]:
            # If we have a situation like A > B > C, we get A > B < C by swapping B and C
            arr[i], arr[i+1] = arr[i+1], arr[i]

        # ">" relation expected
        elif not flag and arr[i] < arr[i+1]:
            # If we have a situation like A < B < C, we get A < C > B by swapping B and C
            arr[i], arr[i+1] = arr[i+1], arr[i]

        i += 1
        flag = not flag


if __name__ == "__main__":
    arr = [4, 3, 7, 8, 6, 2, 1]
    print("the array before convert to zig zag: ", arr)
    zig_zag_array(arr)
    print("the array after convert to zig zag: ", arr)
