class Node(object):

    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class Reverse(object):

    def __init__(self):
        self.head = None
        self.tail = None


    def insert_node(self, node_data):
        node = Node(node_data)

        if self.head == None:
            self.head = node

        else:
            self.tail.next = node
            self.tail.next.prev = self.tail

        self.tail = node


    def reverse_double_linkedlist(self, root):
        prev = None
        curr = root
        next_node = None

        while(curr != None):
            next_node = curr.next
            curr.next = prev
            curr.prev = next_node
            prev = curr
            curr = next_node

        root = prev
        return root


    def print_node(self, root):

        while (root != None):
            print(root.data)
            root = root.next


if __name__ == "__main__":
    double_linked_list = Reverse()
    double_linked_list.insert_node(1)
    double_linked_list.insert_node(2)
    double_linked_list.insert_node(3)
    double_linked_list.insert_node(4)
    double_linked_list.insert_node(5)
    print("before reverse linked list")
    double_linked_list.print_node(double_linked_list.head)
    root = double_linked_list.reverse_double_linkedlist(double_linked_list.head)
    print("After reverse linked list")
    double_linked_list.print_node(root)
