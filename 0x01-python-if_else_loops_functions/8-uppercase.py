#!/usr/bin/python3
def uppercase(str):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    res_string = list()

    for letter in str:
        try:
            char_index = lowercase.index(letter)
            res_string.append(uppercase[char_index])
        except BaseException:
            res_string.append(letter)

    print("{}".format("".join(res_string)))
