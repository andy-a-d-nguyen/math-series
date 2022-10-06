def fibonacci(n):
    """
    Function fibonacci takes in n as a parameter
    and return the nth value in the fibonacci sequence
    :param n: nth number in the fibonacci sequence
    :type n: int
    :returns: nth value in the fibonacci sequence
    :rtype: int
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
