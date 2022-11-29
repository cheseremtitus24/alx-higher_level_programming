#!/usr/bin/python3
import random
number = random.randint(-10, 10)
match number:
    case 0:
        print(f"{number:d} is zero")
    case number if number > 0:
        print(f"{number:d} is positive")
    case number if number < 0:
        print(f"{number:d} is negative")
    case _:
        print("Invalid Number")
