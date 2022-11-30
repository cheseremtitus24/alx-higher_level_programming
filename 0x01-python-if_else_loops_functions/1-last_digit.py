#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def print_val(number, last_digit):
    if last_digit == 0:
        print(f"Last digit of {number} is {last_digit} and is {last_digit}")
    elif last_digit > 5:
        print(f"Last digit of {number} is {last_digit} and is greater than 5")
    elif last_digit < 6:
        str = " and is less than 6 and not 0"
        print(f"Last digit of {number:d} is {last_digit:d}" + str)
    else:
        print(f"Last digit of {number} is {last_digit} and is {last_digit}")


last_digit = None
if number == 0:
    print(f"Last digit of {number} is {number%10:d} and is {number}")
elif number > 0:
    last_digit = number % 10
    print_val(number, last_digit)
elif number < 0:
    last_digit = -number % 10
    last_digit *= -1
    print_val(number, last_digit)
else:
    print("Invalid Number")
