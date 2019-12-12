class Node:
    def __init__(self, data):
        self.data = data
        self. left = None
        self.right = None


def remove_node(root, level, k):
    if root is not None:
        # Using level_left, level_right to save length of node at left and right side
        level_left, level_right = 0,0

        # Calculate length of left side
        if root.left is not None:
            level_left = remove_node(root.left, level+1, k)
            if level_left < k:
                root.left = None

        # Calculate length of right side
        if root.right is not None:
            level_right = remove_node(root.right, level+1, k)
            if level_right < k:
                root.right = None

        # Return max lenth of left side and right side, in case of node leaf return level of this node
        return max(level, level_left, level_right)

    return 0


# Utility method that actually removes the nodes which are not on the pathLen >= k.
# This method can change the root as well.
def remove_node_post_order(root, level, k):
    # Base condition
    if root is None:
        return None

    # Traverse the tree in postorder fashion so that if a leaf node path length is shorter than k, then that node and
    # all of its descendants till the node which are not on some other path are removed.
    root.left = remove_node_post_order(root.left, level+1, k)
    root.right = remove_node_post_order(root.right, level+1, k)

    # If root is a leaf node and it's level is less than k then remove this node. This goes up and check for the
    # ancestor nodes also for the same condition till it finds a node which is a part of other path(s) too.
    if root.left is None and root.right is None and level < k:
        return None

    # Return root
    return root


def inorder_traversal(root):
    if root is not None:

        inorder_traversal(root.left)

        print(root.data)

        inorder_traversal(root.right)


if __name__ == "__main__":
    k = 4
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(7)
    root.right.right = Node(6)
    root.right.right.left = Node(8)

    # print("Before remove node")
    # inorder_traversal(root)
    remove_node(root, 1, k)
    print("after remove node")
    inorder_traversal(root)

