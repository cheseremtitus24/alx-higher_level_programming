#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100 + 1):
        if (i == 100):
            if i % 5 == 0:
                print("{}".format("Buzz"), end=" ")
            else:
                print("{}".format(i), end=" ")

            continue
        else:
            if i % 5 == 0 and i % 3 == 0:
                print("{}".format("FizzBuzz"), end=" ")

            elif i % 5 == 0:
                print("{}".format("Buzz"), end=" ")
            elif i % 3 == 0:
                print("{}".format("Fizz"), end=" ")
            else:
                print("{}".format(i), end=" ")
