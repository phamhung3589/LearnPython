class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to find LCA of n1 and n2. The function assumes that both n1 and n2 are present in BST
def lca(root, val1, val2):
    # Base Case
    if root is None:
        return None

    # If both val1 and val2 are smaller than root, then LCA lies in left
    if root.data > val1 and root.data > val2:
        return lca(root.left, val1, val2)

    # If both val1 and val2 are greater than root, then LCA lies in right
    if root.data < val1 and root.data < val2:
        return lca(root.right, val1, val2)

    return root.data


if __name__ == "__main__":
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)

    root.left.left = Node(4)
    root.left.right = Node(12)

    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    result = lca(root, 10, 14)
    print("lowest common ancestor of node {:d} and node {:d} is: {:d}".format(10, 14, result))
    result = lca(root, 14, 8)
    print("lowest common ancestor of node {:d} and node {:d} is: {:d}".format(14, 8, result))
    result = lca(root, 10, 22)
    print("lowest common ancestor of node {:d} and node {:d} is: {:d}".format(10, 22, result))
