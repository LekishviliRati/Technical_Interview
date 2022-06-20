"""
Recursion is breaking the problem up into smaller and smaller pieces until it can be easily solved.
Recursion function calls itself, and any problem that can be solved recursively can also be solved iteratively,
but in certain cases, recursion offers a more elegant solution.

A recursive algorithm must follow the three laws of recursion:
1. A recursive algorithm must have a base case.
2. A recursive algorithm must change its state and move toward the base case.
3. A recursive algorithm must call itself, recursively.


Problem : Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
For example:
Given num = 55, the process is like: 5 + 5 = 10, 1 + 0 = 1. Since 1 has only one digit, return it.

"""


def add_digits(number):
    """
    :param number: Integer
    :return: Single digit Integer
    """
    number = str(number)
    if len(number) == 1:
        return int(number)
    the_sum = 0
    for c in number:
        the_sum = the_sum + int(c)
    return add_digits(the_sum)


print(add_digits(99))
