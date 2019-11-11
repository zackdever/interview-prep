from myqueue import Node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)

        if not self.top:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if not self.top:
            raise Exception("stack is empty!")

        data = self.top.data
        self.top = self.top.next
        return data

    def __repr__(self):
        items = []
        if self.top:
            item = self.top
            while item:
                items.append(item.data)
                item = item.next
        return '{} top'.format(list(reversed(items)))
