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
