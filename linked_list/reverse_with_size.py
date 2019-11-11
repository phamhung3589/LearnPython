class Node(object):

    def __init__(self, dat):
        self.data = dat
        self.next = None


# program to reverse a linked list in group of given size
class Reverse(object):

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

    def reverse(self, k):
        prev = None
        curr = self.head
        next_node = None

        # Reverse first k nodes of the linked list
        while k > 0 and curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            k -= 1

        # Assign next node of head node to the curr node
        self.head.next = curr

        # prev node is the head of new linked list
        self.head = prev

    def print_node(self):
        curr = self.head

        while curr is not None:
            print(curr.data)
            curr = curr.next


if __name__ == "__main__":
    ll = Reverse()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.insert(6)
    ll.insert(7)
    ll.reverse(7)
    ll.print_node()
