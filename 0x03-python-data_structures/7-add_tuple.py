#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuplen1 = len(tuple_a)
    tuplen2 = len(tuple_b)
    result = list()

    if tuplen1 >= 2 and tuplen2 >= 2:
        paired = zip(tuple_a, tuple_b)
        for index, pair in enumerate(paired):
            if index < 2:
                tupval1 = pair[0] + pair[1]
                result.append(tupval1)
            else:
                break
        return tuple(result)
    elif (tuplen1 < 2):
        result = list(tuple_a)
        result.append(0)
        return add_tuple(tuple(result), tuple_b)
    elif (tuplen2 < 2 and tuplen2 > 0):
        vresult = list(tuple_b)
        vresult.append(0)
        vresult = tuple(vresult)
        return add_tuple(tuple_a, vresult)

    else:
        if tuple_a:
            return tuple_a
        if tuple_b:
            return tuple_b
        return None
