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

    def merge_sorted_linked_list(self, linked_list):
        node_1 = self.head
        node_2 = linked_list.head
        curr = None
        result = None

        if node_1 is None:
            result = node_2

        elif node_2 is None:
            result = node_1

        else:
            if node_1.data < node_2.data:
                curr = node_1
                node_1 = node_1.next
            else:
                curr = node_2
                node_2 = node_2.next

            result = curr

            while node_1 is not None and node_2 is not None:
                if node_1.data < node_2.data:
                    curr.next = node_1
                    node_1 = node_1.next
                else:
                    curr.next = node_2
                    node_2 = node_2.next

                curr = curr.next

            if node_1 is not None:
                curr.next = node_1

            if node_2 is not None:
                curr.next = node_2

        return result

    def print_node(self, root):
        tmp = root
        while tmp is not None:
            print(tmp.data)
            tmp = tmp.next


if __name__ == "__main__":
    ll_1 = LinkedList()
    ll_1.insert(3)
    ll_1.insert(5)
    ll_1.insert(9)
    ll_1.insert(10)
    ll_1.insert(12)
    ll_1.insert(15)

    ll_2 = LinkedList()
    ll_2.insert(1)
    ll_2.insert(2)
    ll_2.insert(4)
    ll_2.insert(6)
    ll_2.insert(11)
    ll_2.insert(18)

    merge__ll = ll_1.merge_sorted_linked_list(ll_2)

    ll_1.print_node(merge__ll)
