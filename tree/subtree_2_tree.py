class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# using inorder to store value inorder of each tree to an array
def inorder(root, arr):
    if root is not None:
        inorder(root.left, arr)

        # Save current element to array
        arr.append(root.data)

        inorder(root.right, arr)


# Check if tree 1 is subtree of tree2
def check_subtree(root1, root2):
    arr1, arr2 = [], []
    inorder(root1, arr1)
    inorder(root2, arr2)

    # using two pointer i and j to iterate throw 2 arr1 and arr2
    i, j = 0, 0

    # First iterator to find the index in arr2 with value equal to the first index in arr1
    while j < len(arr2):
        if arr1[i] != arr2[j]:
            j += 1
        else:
            break

    # Second iterator to check if all element in arr1 in arr2 or not
    while i < len(arr1) and j < len(arr2):
        if arr1[i] != arr2[j]:
            return False

        i += 1
        j += 1

    return True


if __name__ == "__main__":
    root1 = Node("x")
    root1.left = Node("a")
    root1.right = Node("b")
    root1.left.right = Node("c")

    root2 = Node("z")
    root2.right = Node("e")
    root2.right.right = Node("k")
    root2.left = Node("x")
    root2.left.left = Node("a")
    root2.left.right = Node("b")
    root2.left.left.right = Node("c")

    check = check_subtree(root1, root2)
    print("first tree is subtree of second tree: ", check)
