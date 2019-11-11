# Python program to detect and remove loop of linked list
class Node(object):

    # Constructor to initialize the node object
    def __init__(self, dat):
        self.data = dat
        self.next = None


class LinkedList(object):

    # Function to initialize head
    def __init__(self):
        self.head = None
        self.tail = None
        self.save_node = None

    def insert_node(self, dat):
        node = Node(dat)
        if dat == 4:
            self.save_node = node

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def create_loop(self):
        self.tail.next = self.save_node

    def detect_loop(self):
        if self.head is None:
            return False

        # slow and fast runner for detect loop, detect runner for detect the first node in loop
        slow_runner = self.head
        fast_runner = self.head
        detect_runner = self.head

        # using check variable to check if linked list has loop or not
        check = False

        # Search for loop using slow and fast pointers
        while slow_runner.next is not None and fast_runner.next.next is not None:
            # check equal runners
            if slow_runner.next == fast_runner.next.next:
                slow_runner = slow_runner.next
                check = True
                break

            # Move slow and fast 1 and 2 steps respectively
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next

        # if loop exists
        if check:
            while slow_runner.next != detect_runner.next:
                slow_runner = slow_runner.next
                detect_runner = detect_runner.next

            # Remove loop by assigning the next node of last node in loop to None
            slow_runner.next = None

        return check

    # Print linked list after removing loop
    def print_node(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_node(1)
    ll.insert_node(2)
    ll.insert_node(3)
    ll.insert_node(4)
    ll.insert_node(5)
    ll.insert_node(6)
    ll.insert_node(7)
    ll.create_loop()
    ll.detect_loop()
    ll.print_node()
