#!/usr/bin/python3

def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
        result = 0
        for i in range(len(roman_string)):
            # if current item is not the last item on the string
            if i + \
                    1 < len(roman_string) and values[roman_string[i]] < values[roman_string[i + 1]]:
                # and current item's value is smaller than next item's value
                # then subtract current item's value from result
                result = result - values[roman_string[i]]
            else:
                # otherwise add current item's value to result
                result = result + values[roman_string[i]]
        return result
    else:
        return 0
