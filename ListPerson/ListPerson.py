class Node:
    def __init__(self, data: list, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class ListPerson:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def add(self, item: list):
        if not isinstance(item, list):
            return 'incorrect values'
        if len(item) != 2:
            return 'incorrect values'
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

    def add_on_position(self, item: list, position):
        if not isinstance(item, list):
            return 'incorrect values'
        if len(item) != 2:
            return 'incorrect values'
        node = Node(item)
        if self.size == 0:
            self.head = node
            self.tail = node
        if position == 1:
            self.head.next = node
            node.prev = self.head
            self.head = node
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

    def search_for_family(self, family: str):
        if not isinstance(family, str):
            return 'incorrect values'
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
lst.add(['ivanov1', '12.12.12'])
lst.add(['ivanov2', '12.12.12'])
lst.add(['ivanov3', '12.12.12'])
lst.add(['ivanov4', '12.12.12'])
lst.add(['ivanov5', '12.12.12'])
lst.add(['ivanov6', '12.12.12'])
lst.add(['ivanov7', '12.12.12'])
lst.add(['ivanov8', '12.12.12'])
lst.add(['ivanov9', '12.12.12'])
lst.add(['ivanov10', '12.12.12'])
lst.add(['ivanov12', '12.12.12'])
lst.add(['ivanov13', '12.12.12'])
lst.add(['ivanov14', '12.12.12'])
lst.add(['ivanov15', '12.12.12'])
lst.add(['ivanov16', '12.12.12'])
lst.add(['ivanov17', '12.12.12'])
lst.add(['ivanov18', '12.12.12'])
lst.add_on_position(['ivanov333', '12.12.12'], 14)
lst.add_on_position(['ivanov444', '12.12.12'], 14)
lst.add_on_position(['ivanov555', '12.12.12'], 14)
lst.add_on_position(['ivanov_first', '12.12.12'], 1)
lst.add_on_position(['ivanov_last', '12.12.12'], 29)
