from series import fibonacci


def test_fibonacci_0():
    expected = fibonacci(0)
    actual = 0
    assert expected == actual


def test_fibonacci_1():
    expected = fibonacci(1)
    actual = 1
    assert expected == actual


def test_fibonacci_2():
    expected = fibonacci(2)
    actual = 1
    assert expected == actual


def test_fibonacci_3():
    expected = fibonacci(3)
    actual = 2
    assert expected == actual


def test_fibonacci_4():
    expected = fibonacci(4)
    actual = 3
    assert expected == actual


def test_fibonacci_5():
    expected = fibonacci(5)
    actual = 5
    assert expected == actual
