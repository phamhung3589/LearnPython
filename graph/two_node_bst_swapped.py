# Java program to correct the BST if two nodes are swapped
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        # Initialize pointers needed for correctBSTUtil()
        self.first = None
        self.middle = None
        self.last = None
        self.prev = None

    # A function to fix a given BST where two nodes are swapped. This function uses correctBSTUtil() to find out
    # two nodes and swaps the nodes to fix the BST
    def correct_tree(self, root):
        # Set the pointer to find out 2 nodes
        self.correct_tree_util(root)

        # correct the tree
        if self.first and self.last:
            tmp = self.first.data
            self.first.data = self.last.data
            self.last.data = tmp

        # Adjacent nodes swapped
        elif self.first and self.last is None:
            tmp = self.first.data
            self.first.data = self.middle.data
            self.middle.data = tmp

    # This function does inorder traversal to find out the two swapped nodes. It sets three pointers, first, middle
    # and last. If the swapped nodes are adjacent to each other, then first and middle contain the resultant nodes
    # Else, first and last contain the resultant nodes
    def correct_tree_util(self, root):
        if root is not None:
            # Recur for the left subtree
            self.correct_tree_util(root.left)

            # If this node is smaller than the previous node, it's violating the BST rule.
            if self.prev is not None and self.prev.data > root.data:
                # If this is first violation, mark these two nodes as 'first' and 'middle'
                if self.first is None:
                    self.first = self.prev
                    self.middle = root

                # If this is second violation, mark this node as last
                else:
                    self.last = root

            # Mark this node as previous
            self.prev = root

            # Recur for the right subtree
            self.correct_tree_util(root.right)

    # Utility function to print inorder traversal
    def print_node(self, root):
        if root is not None:
            self.print_node(root.left)
            print(root.data)
            self.print_node(root.right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(8)
    root.left.left = Node(2)
    root.left.right = Node(20)
    bst = BinaryTree()

    print("Before correct the tree")
    bst.print_node(root)

    print("After correct the tree")
    bst.correct_tree(root)
    bst.print_node(root)
