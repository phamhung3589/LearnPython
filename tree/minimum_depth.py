class Node:
    def __init__(self, dat):
        self.data = dat
        self.left = None
        self.right = None


def min_depth(root):
    if root is None:
        return 0

    return 1 + min(min_depth(root.left), min_depth(root.right))


# Using BFS to get min depth
def bfs(root):
    # Base case
    if root is None:
        return 0
    # Enqueue root and initialize depth as 1
    q = [{"node": root, "depth": 1}]

    # Do level order traversal
    while len(q) > 0:
        # Remove the front queue item
        node_item = q.pop(0)

        # Get details of the removed item
        node = node_item["node"]
        depth = node_item["depth"]

        # If this is the first leaf node seen so far then return its depth as answer
        if node.left is None and node.right is None:
            return depth

        # If left subtree is not None, add it to queue
        if node.left is not None:
            q.append({"node": node.left, "depth": depth+1})

        # If right subtree is not None, add it to queue
        if node.right is not None:
            q.append({"node": node.right, "depth": depth+1})

    return -1

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    min_d = min_depth(root)
    min_d_bfs = bfs(root)
    print("min depth of this tree using recursive is: ", min_d)
    print("min depth of this tree using bfs is: ", min_d_bfs)