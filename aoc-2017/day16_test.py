import day16


def test_spin_1():
    s = 'abcde'
    assert day16.spin(s, 1) == 'eabcd'


def test_spin_3():
    s = 'abcde'
    assert day16.spin(s, 3) == 'cdeab'


def test_spin_5():
    s = 'abcde'
    assert day16.spin(s, 5) == s


def test_spin_6():
    s = 'abcde'
    assert day16.spin(s, 1) == day16.spin(s, 6)


def test_exchange():
    s = 'abcde'
    assert day16.exchange(s, 1, 2) == 'acbde'


def test_exchange_back():
    s = 'abcde'
    assert day16.exchange(day16.exchange(s, 1, 2), 1, 2) == s


def test_partner_same():
    s = 'abcde'
    assert day16.partner(s, 'a', 'a') == s


def test_partner_swapargs():
    s = 'abcde'
    assert day16.partner(s, 'e', 'a') == day16.partner(s, 'a', 'e')


def test_partner_value():
    s = 'abcde'
    assert day16.partner(s, 'e', 'a') == 'ebcda'


def test_read_input():
    ops = day16.readfile('day16_test_input.txt')
    assert len(ops) == 5
    assert ops[0] == 'pa/c'
    assert ops[4] == 'pn/j'


def test_perform_op_partner():
    seq = 'abcdefghijklmnop'
    ops = ['pa/c']
    assert day16.perform_ops(seq, ops) == 'cbadefghijklmnop'


def test_perform_op_partner_twice():
    seq = 'abcdefghijklmnop'
    ops = ['pa/c', 'pa/c']
    assert day16.perform_ops(seq, ops) == seq


def test_perform_op_partner_spin():
    seq = 'abcdefghijklmnop'
    ops = ['pa/c', 's2']
    assert day16.perform_ops(seq, ops) == 'opcbadefghijklmn'


def test_perform_op_spin_partner():
    seq = 'abcdefghijklmnop'
    ops = ['s2', 'pa/c']
    assert day16.perform_ops(seq, ops) == 'opcbadefghijklmn'
