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







