"""
FizzBuzz Test (Modulo)
Problem :
Write a program that prints the numbers from 1 to 200.
But for multiples of 5 print “Fizz” instead of the number and
for the multiples of 10 print “Buzz”.
For numbers which are multiples of both 5 and 10 print “FizzBuzz”.
"""


def fizz_buzz():
    for i in range(0, 201):
        if i % 5 == 0 and i % 10 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Fizz")
        elif i % 10 == 0:
            print("Buzz")
        else:
            print(i)


fizz_buzz()
