"""
Sequential Search is a simple search algorithm that checks each number in a list one by one to see if it matches
the number we are looking for, or it is looking for.
"""


def sequential_search(any_list, number):

    found = False
    for i in any_list:
        if i == number:
            found = True
            print("Number Found")
            break
    return found


# Will print : Number found and return True
sequential_search(range(0, 10), 7)




