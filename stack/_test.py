from stack import stack


def test_peek():
    assert 6 == stack.peek()


def test_pop():
    assert 6 == stack.pop()


def test_pop2():
    assert 5 == stack.pop()


def test_pop3():
    assert None == stack.pop()


def test_peek2():
    assert None == stack.peek()



