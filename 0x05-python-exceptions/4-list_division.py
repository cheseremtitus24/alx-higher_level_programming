#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = list()
    try:
        for i in range(list_length):
            try:
                result.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            except TypeError:
                print("wrong type")
                result.append(0)
            except IndexError:
                print("out of range")
                # Get the longest list and padd with 0
                length = abs(len(my_list_1) - len(my_list_2))
                for x in range(length):
                    result.append(0)
                break
            except BaseException:
                pass
    except BaseException:
        pass
    else:
        pass
    finally:
        return (result)
