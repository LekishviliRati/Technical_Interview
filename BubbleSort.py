"""
What is a (bubble) sorting algorithm ?
=> It's an algorithm that takes a group of numbers and puts them in a certain order.
"""


def bubble_sort(any_list):
    """
    :param any_list: List of numbers
    :return: Sorted list of numbers
    """
    # In range(len(any_list)-1, 0, -1) first "-1" : starts a for loop that runs the bubble sort algorithm n -1 times.
    # because if there are n items in the list, then there are n - 1 pairs of items that need to be compared on the
    # first pass.
    # " 0 " : Defines a flag variable that will be used to determine if a swap has occurred or not.
    # This is for optimization purposes. The code does not output anything
    # last " -1"  : Starts the inner loop that compares all the values in the list from the first to the last one.
    # The code does not output anything
    for i in range(len(any_list)-1, 0, -1):
        for j in range(i):
            if any_list[j] > any_list[j + 1]:
                temporary_storage_location = any_list[j]
                any_list[j] = any_list[j + 1]
                any_list[j + 1] = temporary_storage_location

    print(any_list)


my_list = [72, 19, 2, 76, 42, 518, 67, 93, 85]
bubble_sort(my_list)


# def see_i_and_j_values(a_list):
#     for i in range(len(a_list) - 1, 0, -1):
#         for j in range(i):
#             print(i)
#             # print(j)
#
#
# false_list = [72, 19, 2, 76, 42, 518, 67, 93, 85]
# see_i_and_j_values(false_list)
