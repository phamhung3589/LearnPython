# Python program to check whether given Binary tree is full or not

# Tree node structure
class Node:
    # Constructor of the node class for creating the node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Checks if the binary tree is full or not
def check_tree(root):
    # If empty tree
    if root is None:
        return True

    # If leaf node
    if root.left is None and root.right is None:
        return True

    # if node left or right is None
    if root.left is None or root.right is None:
        return False

    # If node root has both node left and node right, recursive with node left and node right
    return check_tree(root.left) and check_tree(root.right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)

    root.left.right = Node(40)
    root.left.left = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)

    root.left.left.left = Node(80)
    root.left.left.right = Node(90)
    root.left.right.left = Node(80)
    root.left.right.right = Node(90)
    root.right.left.left = Node(80)
    root.right.left.right = Node(90)
    root.right.right.left = Node(80)
    root.right.right.right = Node(90)

    check = check_tree(root)
    print("is tree a full binary tree:", check)
