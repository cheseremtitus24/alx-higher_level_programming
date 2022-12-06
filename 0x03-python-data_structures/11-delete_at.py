#!/usr/bin/python3
def delete_at(my_list, idx):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        temp_list = list()
        temp_list = my_list[:idx]
        temp_list += my_list[idx+1:]
        my_list = list()

        my_list = temp_list[:]


        return temp_list 
