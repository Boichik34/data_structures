from ListPerson import lst


def test_add_on_position1():
    assert ['ivanov_first', '12.12.12'] == lst.pop(1)


def test_add_on_position2():
    assert ['ivanov_last', '12.12.12'] == lst.pop(lst.size)


def test_add_on_position3():
    assert ['ivanov555', '12.12.12'] == lst.pop(14)


def test_add_on_position4():
    assert ['ivanov444', '12.12.12'] == lst.pop(14)


def test_add_on_position5():
    assert ['ivanov333', '12.12.12'] == lst.pop(14)


def test_pop():
    assert ['ivanov5', '12.12.12'] == lst.pop(5)


def test_pop2():
    assert ['ivanov1', '12.12.12'] == lst.pop(1)


def test_pop3():
    assert ['ivanov18', '12.12.12'] == lst.pop(lst.size)


def test_pop4():
    assert ['ivanov17', '12.12.12'] == lst.pop(lst.size)


def test_add():
    assert 'incorrect values' == lst.add(lst.size)


def test_add2():
    assert 'incorrect values' == lst.add([lst.size, 1, 2])


def test_search_for_family():
    assert "ivanov15's card is number: 12, info: ['ivanov15', '12.12.12']" == lst.search_for_family('ivanov15')


def test_search_for_family2():
    assert "ivanov2's card is number: 1, info: ['ivanov2', '12.12.12']" == lst.search_for_family('ivanov2')


def test_search_for_family3():
    assert "ivanov16's card is number: 13, info: ['ivanov16', '12.12.12']" == lst.search_for_family('ivanov16')


def test_search_for_family4():
    assert "Nothing was found for your request" == lst.search_for_family('ivanov11111')


def test_search_for_family5():
    assert "incorrect values" == lst.search_for_family(2)
