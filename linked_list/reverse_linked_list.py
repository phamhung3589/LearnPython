class Node(object):

    def __init__(self, d):
        self.data = d
        self.next = None

class Reverse(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, node_data):
        node = Node(node_data)

        if self.head == None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def reverse_linkedlist(self, root):
        prev = None
        current = root
        next_node = None

        while current != None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # root = prev
        return prev

if __name__ == "__main__":
    single_linked_list = Reverse()
    single_linked_list.add_node(1)
    single_linked_list.add_node(2)
    single_linked_list.add_node(3)
    single_linked_list.add_node(4)
    single_linked_list.add_node(5)

    root = single_linked_list.reverse_linkedlist(single_linked_list.head)

    while root != None:
        print(root.data)
        root = root.next
		



