"""
Task 2.
Calculates the sum of even numbers of a fibonacci series whose members do not exceed a given value.
"""


def gen_fibonacci_numbers(start=None, end=None):
    """
    Generator that returns Fibonacci numbers.
    If the start elements is not passed, then returns None
    :param start: integer
    :param end: integer
    :return: generator
    """

    if start is None and end is None:
        print('Please indicate the start and end elements of the Fibonacci series')
        return None
    elif start and end is None:
        end = start
    elif start is None and end:
        start = 0

    a = start

    try:
        b = a + 1

        while a <= end:
            yield a
            a, b = b, a + b
    except TypeError as err:
        print(f'Error: {err}. Start and end elements must be integers!')


def get_sum_of_numbers(start=None, end=None):
    """
    Returns the sum of even Fibonacci numbers from :param start: to :param end:
    :param start: integer
    :param end: integer
    :return: integer
    """
    return sum([i for i in gen_fibonacci_numbers(start, end) if i % 2 == 0])


if __name__ == '__main__':
    s = 3
    e = 7000000

    print(list(gen_fibonacci_numbers(s, e)))
    print(get_sum_of_numbers(s, e))
