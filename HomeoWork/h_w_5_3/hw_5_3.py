class Order:
    def __init__(self, id_order: int, price: int, prev=None):
        self.__id_order = id_order
        self.__price = price
        self.prev = prev

    def get_id_order(self):
        return self.__id_order

    def get_price(self):
        return self.__price

    def set_id_order(self, value: int):
        self.__id_order = value

    def set_price(self, value: int):
        self.__price = value

    def __str__(self):
        return f'{self.get_price()}, {self.get_id_order()}'


class OrderQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def place_order(self, order):
        if self.size == 0:
            self.head = order
        else:
            self.tail.prev = order
        self.tail = order
        self.size += 1

    def serve_order(self):
        if self.size == 0:
            return None
        data = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.prev
        self.size -= 1
        return data

    def peek_next_order(self):
        if self.size == 0:
            return None
        return self.head

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def waiting_orders_count(self):
        return self.size


order1 = Order(1, 1)
order2 = Order(2, 2)
order3 = Order(3, 3)
order4 = Order(4, 4)
order5 = Order(5, 5)
order6 = Order(6, 6)
order7 = Order(7, 7)
order_queue = OrderQueue()
order_queue.place_order(order1)
order_queue.place_order(order2)
order_queue.place_order(order3)
order_queue.place_order(order4)
order_queue.place_order(order5)
order_queue.place_order(order6)
order_queue.place_order(order7)


class Request:
    def __init__(self, request_id: int, description: str, priority: int, prev=None):
        self.request_id = request_id
        self.description = description
        self.priority = priority
        self.prev = prev

    def __str__(self):
        return f'{self.request_id}, {self.request_id}'


class SupportQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def submit_request(self, request):
        if self.size == 0:
            self.head = request
            self.tail = request
            self.size += 1
        else:
            self.tail.prev = request
            self.tail = request
            self.size += 1

    def resolve_request(self):
        if self.size == 0:
            return None
        if self.size == 1:
            data = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return data
        number = 0
        priority = 0
        target_link = self.head
        for i in range(self.size):

            if target_link.priority > priority:
                priority = target_link.priority
                number = i
            target_link = target_link.prev

        return self.del_request(number)

    def del_request(self, number):
        if number == 0:
            data = self.head
            self.head = self.head.prev
            self.size -= 1
            return data
        targrt_link = self.head
        for i in range(number):
            targrt_link = targrt_link.prev
        data = targrt_link
        self.size -= 1
        return data

    def peek_next_request(self):
        data = 0
        priority = 0
        target_link = self.head
        for i in range(self.size):
            if target_link.priority > priority:
                priority = target_link.priority
                data = target_link
            target_link = target_link.prev
        return data

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False


support_tqueue = SupportQueue()
request1 = Request(1, '1', 17)
request2 = Request(2, '2', 8)
request3 = Request(3, '3', 9)


