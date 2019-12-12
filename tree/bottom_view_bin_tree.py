# Top view of a binary tree is the set of nodes visible when the tree is viewed from the top.
# Given a binary tree, print the top view of it.


# Base class for saving node in tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Get bottom view of the tree
def image_tree(root):
    # Using hash table to store (key=order, value=[node.data, level])
    hash_table = dict()
    # Using queue to iterate through all node in the tree using bfs
    q = [{"node": root, "level": 0, "order": 0}]

    while len(q) != 0:
        # Get the first node in queue
        item = q.pop(0)
        node, level, order = item["node"], item["level"], item["order"]

        # Check if order not in tree - push [data, order] as the value of key: order in hash table
        if order not in hash_table:
            hash_table[order] = [node.data, level]

        # Else if order in hash table
        else:
            # Check if level of current node larger than the level in hash table or not
            # If yes, replace [data, level] or order in hash table by value of current node -
            # because node with higher level with hide the node with lower level if see from the bottom
            if hash_table[order][1] < level:
                hash_table[order] = [node.data, level]

        # Check node left is None or not and push to queue
        if node.left is not None:
            q.append({"node": node.left, "level": level+1, "order": order-1})

        # Check node right is None or not and push to queue
        if node.right is not None:
            q.append({"node": node.right, "level": level+1, "order": order+1})

    # Sort hash table with order and return value corresponding
    result = [hash_table[ele][0] for ele in sorted(hash_table.keys())]

    return result


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right.right = Node(6)

    root.left.right.left = Node(7)
    root.left.right.right = Node(8)

    bottom_view = image_tree(root)
    print(bottom_view)
