"""
-------------------------------------------------------------------------------
Name:		statTools.py
Purpose:		
4 Types of functions
Median: outputs the middle number of a list.
Range: outputs the difference between largest and smallest number of a list/
Variance: outputs the difference between each number and mean of a list is appended to a new list, then is calculated 
again by adding all the new numbers together and dividing it by the length of the new list.
Standard Deviation: same as variance except output number is square rooted

Author:		Ru. E

Created:	11/11/2018
------------------------------------------------------------------------------
"""

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
