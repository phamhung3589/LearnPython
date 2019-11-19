class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:

    max_result = 0

    # Base Case
    def max_path(self, root):
        if root is None:
            return 0

        # l and r store maximum path sum going through left and right child of root respectively
        l = self.max_path(root.left)
        r = self.max_path(root.right)

        # Max path for parent call of root. This path must include at most one child of root
        max_side = max(max(l, r) + root.data, root.data)

        # Max top represents the sum when the node under consideration is the root of the maxSum path and no ancestor
        # of root are there in max sum path
        max_top = max(max_side, l + r + root.data)

        # Static variable to store the changes Store the maximum result
        self.max_result = max(self.max_result, max_top)

        return max_side


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)

    tree = Tree()
    tree.max_path(root)
    print("the max path in this tree is: ", tree.max_result)
