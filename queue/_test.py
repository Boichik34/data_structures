from queue1 import queue


def test_peek():
    assert 111 == queue.peek()


def test_dequeue():
    assert 111 == queue.dequeue()


def test_dequeue2():
    assert 1 == queue.dequeue()


def test_peek2():
    assert 2 == queue.peek()


def test_dequeue3():
    assert 2 == queue.dequeue()


def test_is_empty():
    assert True == queue.is_empty()


def test_dequeue4():
    assert None == queue.dequeue()