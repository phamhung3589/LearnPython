# Python3 program to reverse alternate levels of a tree


# A Binary Tree Node Utility function to create a new tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_inorder(root):
    if root is not None:
        print_inorder(root.left)
        print(root.data)
        print_inorder(root.right)


def reverse_tree(root):
    queue1 = [root]
    flag = 1

    while queue1[0].left is not None:
        queue2 = []
        for node in queue1:
            queue2.append(node.left)
            queue2.append(node.right)

        if flag % 2 == 0:
            i = 0
            for node in queue1[::-1]:
                node.left = queue2[i]
                node.right = queue2[i+1]
                i += 2
        else:
            i = len(queue2) - 1
            for node in queue1:
                node.left = queue2[i]
                node.right = queue2[i-1]
                i -= 2

        queue1 = queue2
        flag += 1


def reverse_tree_preorder(left, right, level):
    # Base cases
    if left is None and right is None:
        return

    # Swap subtrees if level is even
    if level % 2 == 0:
        tmp = left.data
        left.data = right.data
        right.data = tmp

    # Recur for left and right subtrees (Note : left of root1 is passed and right of root2 in first call and
    # opposite in second call.
    reverse_tree_preorder(left.left, right.right, level+1)
    reverse_tree_preorder(left.right, right.left, level+1)


if __name__ == "__main__":
    root = Node("a")
    root.left = Node('b')
    root.right = Node('c')
    root.left.left = Node('d')
    root.left.right = Node('e')
    root.right.left = Node('f')
    root.right.right = Node('g')
    root.left.left.left = Node('h')
    root.left.left.right = Node('i')
    root.left.right.left = Node('j')
    root.left.right.right = Node('k')
    root.right.left.left = Node('l')
    root.right.left.right = Node('m')
    root.right.right.left = Node('n')
    root.right.right.right = Node('o')

    print("Before reverse node in perfect binary tree")
    print_inorder(root)

    # reverse_tree(root)
    reverse_tree_preorder(root.left, root.right, 0)
    print("After reverse node in perfect binary tree")
    print_inorder(root)
