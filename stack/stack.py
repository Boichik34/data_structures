class Node:
    def __init__(self, data, prev=None):
        self.data = data
        self.prev = prev


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        self.top = Node(item, self.top)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        else:
            data = self.top.data
            self.top = self.top.prev
            self.size -= 1
            return data

    def peek(self):
        if self.size == 0:
            return None
        else:
            return self.top.data

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False


stack = Stack()

stack.push(5)
stack.push(6)

