def fibonacci(n):
    """
    Function fibonacci takes in n as a parameter
    and return the nth value in the Fibonacci sequence
    :param n: nth number in the Fibonacci sequence
    :type n: int
    :returns: nth value in the Fibonacci sequence
    :rtype: int
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
    Function lucas takes in n as a parameter
    and return the nth value in the Lucas series
    :param n: nth number in the Lucas series
    :type n: int
    :return: nth value in the Lucas series
    :rtype: int
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, first_optional_param=0, second_optional_param=1):
    """
    sum_series, if called with only one parameter n, will produce the nth value
    in the Fibonacci sequence. If called with 2 as second parameter and
    1 as third parameter, it will produce the nth value in the Lucas series.
    Otherwise, it will calculate a series based on the second and third parameters
    :param n: nth number in a related series of number
    :type n: int
    :param first_optional_param: if left blank along with second_optional_param,
    defaults to Fibonacci sequence. If set to 2 while second_optional_param is set to 1,
    defaults to Lucas series. Otherwise, a new series is calculated
    :type first_optional_param: int
    :param second_optional_param: if left blank along with second_optional_param,
    defaults to Fibonacci sequence. If set to 1 while first_optional_param is set to 2,
    defaults to Lucas series. Otherwise, a new series is calculated
    :type second_optional_param: int
    :return: nth value in a related series of number
    :rtype: int
    """
    if first_optional_param == 0 and second_optional_param == 1:
        return fibonacci(n)
    elif first_optional_param == 2 and second_optional_param == 1:
        return lucas(n)
    else:
        num1 = first_optional_param
        num2 = second_optional_param
        total = 0
        for i in range(1, n):
            total = num1 + num2
            num1 = num2
            num2 = total
        return total
