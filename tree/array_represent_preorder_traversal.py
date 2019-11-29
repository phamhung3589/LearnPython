def check_preorder_brute_force(arr, start, end):
    if start >= end:
        return True

    m = find_value(arr, start, end)
    if m == -1:
        return False

    return check_preorder_brute_force(arr, start + 1, m-1) and check_preorder_brute_force(arr, m, end)


def find_value(arr, start, end):
    index = start

    for i in range(start+1, end+1):
        if arr[i] > arr[start]:
            index = i
            break

    for i in range(index, end+1):
        if arr[i] < arr[start]:
            return -1

    return index


def check_order_optimize(arr):
    # Initialize current root as minimum possible value
    root = float("-inf")
    # Create an empty stack
    stack = []

    # Traverse given array
    for value in arr:

        # If we find a node who is on the right side and smaller than root, return False
        if value < root:
            return False

        # If value(pre[i]) is in right subtree of stack top, Keep removing items smaller than value and make the
        # last removed items as new root
        while len(stack) > 0 and stack[-1] < value:
            root = stack.pop()

        # At this point either stack is empty or value is smaller than root, push value
        stack.append(value)

    return True


if __name__ == "__main__":
    arr = [7, 4, 2, 1, 3, 5, 6, 10, 8, 9, 12, 11, 13]
    result = check_preorder_brute_force(arr, 0, len(arr)-1)
    result_optimize = check_order_optimize(arr)

    print("This array can represent as a preorder of binary search tree: ", result)
    print("This array can represent as a preorder of binary search tree using optimize approach: ", result_optimize)
