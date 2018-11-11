"""
-------------------------------------------------------------------------------
Name:		statTools.py
Purpose:
(Mean):
Add all integers in a given list and divide the total by the amount of integers
in the list. Return the result.

Author:		Lau.A

Created:		09/09/2018
------------------------------------------------------------------------------
"""

def mean(my_list):
    try:
        total = 0
        if len(my_list) == 0:
            return "Error: Empty List"
        for i in range(len(my_list)):
            total += my_list[i]
        return total/len(my_list)
    except TypeError:
        return "Error: TypeError"

def mode(my_list):
    count = 0
    mode = None
    mode2 = None
    for i in my_list:
        max_occurences = my_list.count(i)
        if max_occurences > count:
            count = max_occurences
            mode = i
        if max_occurences == count:
            mode2 = i
    if len(my_list) == 0:
        return "Error: Empty List"
    elif len(my_list) == 1:
        return my_list[0]
    if mode != mode2:
        return "There is no unique mode"
    else:
        return mode

def lower_quartile(my_list):
    new_list = []
    my_list.sort()
    if len(my_list) == 0:
        return "Error: Empty List"
    if len(my_list) % 2 == 0 and len(my_list) % 4 == 0:
        new_list = my_list[:int(len(my_list)/2)]
        new_list = new_list[:int(len(new_list)/2)+1]
        median = (new_list[len(new_list)-1] + new_list[len(new_list)-2]) / 2
        return median
    elif len(my_list) % 2 == 0 and len(my_list) % 4 != 0:
        new_list = my_list[:int(len(my_list) / 2)]
        new_list = new_list[:int(len(new_list) / 2) + 1]
        median = new_list[len(new_list)-1]
        return median
    elif len(my_list) % 2 != 0:
        new_list = my_list[:int(len(my_list) / 2)]
        new_list = new_list[:int(len(new_list) / 2) + 1]
        median = new_list[len(new_list)-1]
        return median









