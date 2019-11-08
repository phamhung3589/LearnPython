class Node(object):

    def __init__(self, dat):
        self.data = dat
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, dat):
        node = Node(dat)

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    # merge 2 linked list into linked list 1
    def merge_2_linked_list(self, node_2_ll):

        # get node_1 and node_2 to head node
        node_2 = node_2_ll.head
        node_1 = self.head

        # while there are available position for node 1 and node 2
        while node_1 is not None and node_2 is not None:
            # assign node_2 to tmp node and node_2 to node_2.next
            tmp = node_2
            node_2 = node_2.next

            # assign next of tmp (=node_2.next) to node_1.next
            tmp.next = node_1.next

            # Assign tmp node (node2) to node_1.next
            node_1.next = tmp

            # assign node1 to next of node 1 (tmp.next)
            node_1 = tmp.next

        # Assign head of node 2 to the next node in node_2 above
        node_2_ll.head = node_2

    def print_node(self):
        node_1 = self.head

        while node_1 is not None:
            print(node_1.data)
            node_1 = node_1.next


if __name__ == "__main__":
    node_1 = LinkedList()
    node_1.insert(1)
    node_1.insert(2)
    node_1.insert(3)

    node_2 = LinkedList()
    node_2.insert(4)
    node_2.insert(5)
    node_2.insert(6)
    node_2.insert(7)
    node_2.insert(8)

    node_1.merge_2_linked_list(node_2)
    print("node 1 is ")
    node_1.print_node()

    print("node 2 is :")
    node_2.print_node()
