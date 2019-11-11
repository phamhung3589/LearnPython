class Node(object):

    def __init__(self, dat):
        self.data = dat
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    # insert node into linked list
    def insert(self, dat):
        node = Node(dat)

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def merge_sort(self, root):
        # Base case : if head is null
        if root is None or root.next is None:
            return root

        # get the middle of the list
        middle = self.get_middle(root)
        middle_next = middle.next

        # set the next of middle node to null
        middle.next = None

        # Apply mergeSort on left list
        left_node = self.merge_sort(root)

        # Apply mergeSort on right list
        right_node = self.merge_sort(middle_next)

        # Merge the left and right lists
        result = self.merge(left_node, right_node)

        return result

    def merge(self, node_1, node_2):

        # Base cases
        if node_1 is None:
            return node_2

        if node_2 is None:
            return node_1

        result = None

        # Pick either a or b, and recur
        if node_1.data < node_2.data:
            result = node_1
            result.next = self.merge(node_1.next, node_2)

        else:
            result = node_2
            result.next = self.merge(node_1, node_2.next)

        return result

    # Utility function to get the middle of the linked list using slow and fast runner
    def get_middle(self, root):
        slow = root
        fast = root

        while fast.next.next is not None:
            slow = slow.next
            fast = fast.next

        return slow

    # Print linked list
    def print_node(self, root):
        tmp_node = root
        while tmp_node is not None:
            print(tmp_node.data)
            tmp_node = tmp_node.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(3)
    ll.insert(7)
    ll.insert(5)
    ll.insert(6)
    ll.insert(10)
    ll.insert(4)
    ll.insert(9)
    ll.insert(8)
    sorted_linked_list = ll.merge_sort(ll.head)
    ll.print_node(sorted_linked_list)
