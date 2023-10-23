class Node:
    def __init__(self, data, prev=None):
        self.data = data
        self. prev = prev


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, item, prev=None):
        noda = Node(item)
        if self.size == 0:
            self.head = noda
        else:
            self.tail.prev = noda
        self.tail = noda
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        data = self.head.data
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.prev
        self.size -= 1
        return data

    def peek(self):
        if self.size == 0:
            return None
        else:
            return self.head.data

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

