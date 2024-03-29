class Node(object):

    # Constructor to initialize the node object
    def __init__(self, dat):
        self.data = dat
        self.next = None


# Python program to insert in a sorted list
class LinkedList(object):

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Utility function to print it the linked LinkedList
    def print_node(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next

    def insert_sorted_linkedlist(self, dat):
        new_node = Node(dat)

        # Special case for the empty linked list
        if self.head is None or self.head.data > dat:
            new_node.next = self.head
            self.head = new_node

        else:
            # Locate the node before the point of insertion
            curr = self.head
            while curr.next is not None and curr.next.data < dat:
                curr = curr.next

            new_node.next = curr.next
            curr.next = new_node


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_sorted_linkedlist(3)
    ll.insert_sorted_linkedlist(4)
    ll.insert_sorted_linkedlist(6)
    ll.insert_sorted_linkedlist(5)
    ll.insert_sorted_linkedlist(7)
    ll.insert_sorted_linkedlist(1)
    ll.print_node()
