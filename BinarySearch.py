"""
Binary Search is a logarithmic algorithm used to search for numbers in a list, numbers have to be ordered.
BS works by cutting the list in half, it picks a number in the middle of the list, and looks at whether it's the right
number or not. It works by throwing away everything above or below the number we are looking for.
"""


def binary_search(any_integer_ordered_list, any_required_number):
    """
    :param any_integer_ordered_list: any list of ordered integers we need to use.
    :param any_required_number: any integer to search for in the list.
    :return: True if the number is find otherwise False
    """

    first = 0
    last = len(any_integer_ordered_list)-1
    number_found = False

    while first <= last and not number_found:
        # I / is used instead of //, a "TypeError: list indices must be integers, not float" will occur.
        middle_of_list = (first + last) // 2
        if any_integer_ordered_list[middle_of_list] == any_required_number:
            number_found = True
            # print("Required number found")
        else:
            if any_required_number < any_integer_ordered_list[middle_of_list]:
                last = middle_of_list - 1
            else:
                first = middle_of_list + 1

    return number_found


ordered_integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

is_7_in_list = binary_search(ordered_integer_list, 7)
print(is_7_in_list)
