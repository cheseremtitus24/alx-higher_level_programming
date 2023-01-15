#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b0 = Base(0)
    print(b0.id)

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
