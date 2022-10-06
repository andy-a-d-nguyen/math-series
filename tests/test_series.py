from series import fibonacci, lucas, sum_series


def test_fibonacci_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fibonacci_3():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fibonacci_4():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


def test_fibonacci_5():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_2():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_lucas_3():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_sum_series_n_equals_5_no_optional_params():
    actual = sum_series(5)
    expected = 5
    assert actual == expected


def test_sum_series_n_equals_6_no_optional_params():
    actual = sum_series(6)
    expected = 8
    assert actual == expected


def test_sum_series_n_equals_5_with_optional_params_2_and_1():
    actual = sum_series(5, 2, 1)
    expected = 11
    assert actual == expected


def test_sum_series_n_equals_6_with_optional_params_2_and_1():
    actual = sum_series(6, 2, 1)
    expected = 18
    assert actual == expected


def test_sum_series_with_other_series():
    actual = sum_series(3, 2, 3)
    expected = 8
    assert actual == expected
