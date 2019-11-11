import random
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

    # Get length of linkedlist with index from 0 to n-1
    def get_len(self):
        root = self.head
        len_ll = -1

        while root is not None:
            root = root.next
            len_ll += 1

        return len_ll

    # using random.randint function to choose the random node
    def select_random_node(self):
        root = self.head
        len_node = self.get_len()

        # Choose the random index from 0 to len
        index = random.randint(0, len_node)

        # select random node corresponding to the index
        while index > 0:
            root = root.next
            index -= 1

        return root


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(3)
    ll.insert(5)
    ll.insert(10)
    ll.insert(4)
    ll.insert(7)
    ll.insert(8)
    print(ll.select_random_node().data)
    print(ll.select_random_node().data)
    print(ll.select_random_node().data)
    print(ll.select_random_node().data)
