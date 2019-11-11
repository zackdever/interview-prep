class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enque(self, item):
        node = Node(item)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def deque(self):
        if not self.head:
            raise Exception("queue is already empty")

        item = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return item

    def __repr__(self):
        items = []
        if self.head:
            item = self.head
            while item:
                items.append(item.data)
                item = item.next
        return "H {} T".format(str(items))
