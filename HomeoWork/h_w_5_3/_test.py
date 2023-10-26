from hw_5_3 import order_queue
from hw_5_3 import order1


def test_peek_next_order():
    assert order1 == order_queue.peek_next_order()

