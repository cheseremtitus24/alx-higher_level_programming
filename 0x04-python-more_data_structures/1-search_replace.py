#!/usr/bin/python3

def search_replace(my_list, search, replace):
    mylist = list()
    # mylist = my_list[:]

    mylist = my_list.copy()
    # for item in my_list:

    #    mylist.append(item)

    if mylist.count(search) >= 1:
        for x in range(mylist.count(search)):
            mylist[mylist.index(search)] = replace
        return mylist
    return mylist
