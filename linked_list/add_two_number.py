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


# get value from linked list of num
def get_num(num):
    # Base case when num is None
    if num is None:
        return ""
    # Convert num from int to string and + recursive for num.next
    return str(num.data) + get_num(num.next)


# Get sum of 2 number: num_1 and num_2
def get_sum(num_1, num_2):
    new_num = LinkedList()
    a = str(int(get_num(num_1)) + int(get_num(num_2)))
    for i in a:
        new_num.insert(int(i))

    return new_num.head


if __name__ == "__main__":
    # num_1 = 563
    num_1 = LinkedList()
    num_1.insert(5)
    num_1.insert(6)
    num_1.insert(3)

    # num_2 = 742
    num_2 = LinkedList()
    num_2.insert(7)
    num_2.insert(4)
    num_2.insert(2)

    # sum_num = 563 + 742 = 1305
    sum_num = get_sum(num_1.head, num_2.head)

    while sum_num is not None:
        print(sum_num.data)
        sum_num = sum_num.next
