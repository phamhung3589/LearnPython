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

    def delete_node(self, dat):
        curr = self.head

        # if the element to be deleted is at the top
        if curr.data == dat:
            if curr.next is not None:
                curr = curr.next
                self.head = curr
            else:
                self.head = None

            return

        # if not at top then we will search it one by one.
        else:
            while curr.next.data != dat:
                curr = curr.next

            curr.next = curr.next.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_sorted_linkedlist(3)
    ll.insert_sorted_linkedlist(4)
    ll.insert_sorted_linkedlist(6)
    ll.insert_sorted_linkedlist(5)
    ll.insert_sorted_linkedlist(7)
    ll.insert_sorted_linkedlist(1)
    ll.print_node()
    print("delete node 1")
    ll.delete_node(1)
    ll.print_node()
    print("delete node 4")
    ll.delete_node(4)
    ll.print_node()
    print("delete node 7")
    ll.delete_node(7)
    ll.print_node()

