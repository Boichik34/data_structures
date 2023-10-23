class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class ListPerson:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def add(self, item):
        node = Node(item)
        if self.size == 0:
            self.head = node
        else:
            self.tail.prev = node
            node.next = self.tail
        self.tail = node
        self.size += 1

    def pop(self, position: int):
        if position > self.size or position < 1:
            return None
        elif position == self.size:
            data = self.tail.data
            self.tail.prev = None
            self.tail = self.tail.next
        else:
            if self.size == 1:
                data = self.head.data
                self.head = None
                self.tail = None
            else:
                if position >= self.size / 2:
                    target_link = self.tail
                    for i in range(self.size - position):
                        target_link = target_link.next # link
                    del_el = target_link.next # element
                    data = target_link.data
                    del_el_p = target_link.prev
                    del_el_p.next = target_link.next
                    del_el.prev = target_link.prev
                else:
                    if position == 1:
                        data = self.head.data
                        self.head = self.head.prev
                    else:
                        target_link = self.head
                        for i in range(position - 1):
                            target_link = target_link.prev
                        data = target_link.data
                        del_el_prev = target_link.prev
                        del_el_next = target_link.next
                        del_el_next.prev = target_link.prev
                        del_el_prev.next = target_link.next
        self.size -= 1
        return data

    def add_on_position(self, item, position):
        node = Node(item)
        if self.size == 0:
            self.head = node
            self.tail = node

        if position > self.size:
            self.tail.prev = node
            node.next = self.tail
            self.tail = node
        else:
            if self.size / 2 <= position:
                target_link = self.tail
                for i in range(self.size - position):
                    target_link = target_link.next
                node.next = target_link.next
                node.next.prev = node
                node.prev = target_link
                target_link.next = node
        self.size += 1

    def search_for_family(self, family):
        if self.size == 0:
            return 'list is empty'
        target_link = self.head
        for i in range(self.size):
            data = target_link.data
            if data[0] == family:
                return f"{family}'s card is number: {i+1}, info: {data}"
            else:
                target_link = target_link.prev

        return "Nothing was found for your request"

lst = ListPerson()

