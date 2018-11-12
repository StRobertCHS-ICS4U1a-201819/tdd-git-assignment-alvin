"""
-------------------------------------------------------------------------------
Name:		statTools.py
Purpose:
The purpose of this file is to contain the central tendency functions and
spread functions.

Authors:		Lau.A, Ru.E

Created:		11/11/2018
------------------------------------------------------------------------------
"""

def mean(my_list):
    '''Adds all integers in a given list and divide the total by the amount of
    integers in the list Return the result.

     :param my_list: the list of integers to find the mean from
     :return: returns the mean of the list
     '''

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
    '''Finds the mode of the list of integers and returns it.

     :param my_list: the list of integers to find the mode from
     :return: returns the mode of the list
     '''

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
    '''Finds the median of the lower half of the list of integers.
    Specific function procedure: Cuts the list so that only the first 1/4th
    of the list remains. Then it finds and returns the area that is cut.

     :param my_list: the list of integers to find the lower quartile from
     :return: returns the lower quartile of the list
     '''

    try:
        my_list.sort()
        if len(my_list) == 0:
            return "Error: Empty List"
        elif len(my_list) < 2:
            return "No upper or lower quartile"
        if len(my_list) % 2 == 0 and len(my_list) % 4 == 0:
            my_list = my_list[:int(len(my_list)/4)+1]
            return (my_list[len(my_list)-1] + my_list[len(my_list)-2])/2
        elif len(my_list) % 2 == 0 and len(my_list) % 4 != 0:
            my_list = my_list[:int(len(my_list)/4)+1]
            return my_list[len(my_list)-1]
        elif len(my_list) % 2 != 0:
            my_list = my_list[:int(len(my_list)/4)+1]
            return my_list[len(my_list)-1]
    except TypeError:
        return "Error: TypeError"

def upper_quartile(my_list):
    '''Finds the median of the upper half of the list of integers.
    Specific function procedure: Cuts the list so that only the last 1/4th
    of the list remains. Then it finds and returns the area that is cut.

     :param my_list: the list of integers to find the upper quartile from
     :return: returns the upper quartile of the list
     '''

    try:
        my_list.sort()
        if len(my_list) == 0:
            return "Error: Empty List"
        elif len(my_list) < 2:
            return "No upper or lower quartile"
        if len(my_list) % 2 == 0 and len(my_list) % 4 == 0:
            my_list = my_list[int(len(my_list)*(3/4)-1):]
            return (my_list[0] + my_list[1])/2
        elif len(my_list) % 2 == 0 and len(my_list) % 4 != 0:
            my_list = my_list[int(len(my_list) * (3 / 4)):]
            return my_list[0]
        elif len(my_list) % 2 != 0:
            my_list = my_list[int(len(my_list) * (3 / 4)):]
            return my_list[0]
    except TypeError:
        return "Error: TypeError"
#========================================
import math


def median(num):

    if len(num) % 2 == 1:
        num = num[(int(len(num)/2))]

    elif len(num) == 0:
        return "Error: Empty List"

    else:
        num = (num[int(len(num)/2) - 1] + num[int(len(num)/2)])/2

    return num


def ranges(num):

    num_list = list(num)

    if len(num_list) >= 2:
        return num_list[len(num_list) - 1] - num_list[0]

    elif len(num_list) == 1:
        return num_list[0]

    else:
        return "Error: Empty List"


def variance(num):

    num_list = list(num)
    len_list = len(num_list)
    list_mean_diff = []
    list_squared = []

    try:
        if len_list == 0:
            return "Error: Empty List"

        elif len_list == 1:
            return "Error: List must have 2 or more integers"

        elif len_list >= 2:
            mean = sum(num_list) / len(num_list)
            a = 0
            while a <= len_list - 1:
                x = num_list[a] - mean
                list_mean_diff.append(x)
                a = a + 1

            b = 0
            while b <= len_list - 1:
                y = list_mean_diff[b] * list_mean_diff[b]
                list_squared.append(y)
                b = b + 1

            sum_list_squared = sum(list_squared)
            number = (sum_list_squared / len_list)

            return number

    except TypeError:
        return "Error: Type Error"



def standard_deviation(num):

    num_list = list(num)
    len_list = len(num_list)
    list_mean_diff = []
    list_squared = []

    try:
        if len_list == 0:
            return "Error: Empty List"

        elif len_list == 1:
            return "Error: List must have 2 or more integers"

        elif len_list >= 2:
            mean = sum(num_list) / len(num_list)
            a = 0
            while a <= len_list - 1:
                x = num_list[a] - mean
                list_mean_diff.append(x)
                a = a + 1

            b = 0
            while b <= len_list - 1:
                y = list_mean_diff[b] * list_mean_diff[b]
                list_squared.append(y)
                b = b + 1

            sum_list_squared = sum(list_squared)
            number = (sum_list_squared / len_list)

            return float((math.sqrt(number)))

    except TypeError:
        return "Error: Type Error"
