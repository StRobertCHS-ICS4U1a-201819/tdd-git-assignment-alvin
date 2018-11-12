<<<<<<< HEAD
"""
-------------------------------------------------------------------------------
Name:		test_statTools.py
Purpose:
The purpose of this file is to contain assert functions to test the functionality
of the central tendency and spread functions that are located in the statTools.py file.

Authors:		Lau.A, Ru.E

Created:		11/11/2018
------------------------------------------------------------------------------
"""

import pytest
from statTools import *

#MEAN GENERAL CASE:
#general case: sorted list
def test_mean_basic1():
    assert(mean([1, 2, 4, 7, 8]) == 4.4)

#general case: unsorted list
def test_mean_basic2():
    assert(mean([7, 1, 3, 0, 0, 1]) == 2)

#general case: list with negative integers included
def test_mean_basic3():
    assert(mean([3, 1, -4, 1, -6, 2]) == -0.5)

#corner case: list of 1 integer
def test_mean_corner1():
    assert(mean([0]) == 0)

#MEAN CORNER CASE:
#corner case: empty list
def test_mean_corner2():
    assert(mean([]) == "Error: Empty List")

#MEAN UNUSUAL CASE:
#unusual case: string input
def test_mean_unusual():
    assert(mean(["2", "4", "7", "3"]) == "Error: TypeError")

#MODE GENERAL CASE:
#general case: sorted list
def test_mode_basic1():
    assert(mode([1, 2, 2, 4, 5, 7, 8]) == 2)

#general case: unsorted list
def test_mode_basic2():
    assert(mode([5, 1, 2, 7, 2, 8, 4]) == 2)

#general case: list with negative integers included
def test_mode_basic3():
    assert(mode([1, 4, 3, -5, -1, 4, 2]) == 4)

#general case: more than one mode
def test_mode_basic4():
    assert(mode([1, 3, 2, 3, 1, 4, 4, 5]) == "There is no unique mode")

#MODE CORNER CASE:
#corner case: empty list
def test_mode_corner():
    assert(mode([]) == "Error: Empty List")

#corner case: list of one integer
def test_mode_corner2():
    assert(mode([1]) == 1)

#MODE UNUSUAL CASE:
#unusual case: list with integers and strings
def test_mode_unusual():
    assert(mode(["3", "1", "5", 1, "7", 3]) == "There is no unique mode")

#unusual case: list with integers and strings
def test_mode_unusual2():
    assert (mode(["3", "f", 7, ".", "r", "g", 3, "."]) == ".")

#LOWER QUARTILE GENERAL CASE:
#genercal case: sorted list (length of list is even)
def test_lower_quartile_basic1():
    assert(lower_quartile([1, 1, 2, 4, 5, 5, 7, 8]) == 1.5)

#general case: unsorted list (length of list is even)
def test_lower_quartile_basic2():
    assert(lower_quartile([12, 5, 22, 30, 7, 36, 14, 42, 15, 53, 25, 65]) == 13)

#general case: sorted list (remainder when divided by 4)
def test_lower_quartile_basic3():
    assert(lower_quartile([1, 2, 3, 4, 5, 6, 6, 7, 8, 8]) == 3)

#general case: unsorted list with negative integers (length of list is odd)
def test_lower_quartile_basic4():
    assert(lower_quartile([-12, 5, -22, 30, 7, -36, 14, 42, - 15, 53, 25]) == -15)

#LOWER QUARTILE CORNER CASE:
#corner case: empty list
def test_lower_quartile_corner1():
    assert(lower_quartile([]) == "Error: Empty List")

#corner case: list of 1 integer
def test_lower_quartile_corner2():
    assert(lower_quartile([1]) == "No upper or lower quartile")

#LOWER QUARTILE UNUSUAL CASE:
#unusual case: list with integers and strings
def test_lower_quartile_unusual():
    assert(lower_quartile(["p", "f", 3, "12", "."]) == "Error: TypeError")

#unusual case: list with integers and strings
def test_lower_quartile_unusual2():
    assert(lower_quartile(["good morning", 13, "!?", 7, 3]) == "Error: TypeError")

#UPPER QUARTILE GENERAL CASE:
#genercal case: sorted list (length of list is even)
def test_upper_quartile_basic1():
    assert(upper_quartile([1, 1, 2, 4, 5, 5, 7, 8]) == 6)

#general case: unsorted list (length of list is even)
def test_upper_quartile_basic2():
    assert(upper_quartile([12, 5, 22, 30, 7, 36, 14, 42, 15, 53, 25, 65]) == 39)

#general case: sorted list (remainder when divided by 4)
def test_upper_quartile_basic3():
    assert(upper_quartile([1, 2, 3, 4, 5, 6, 6, 7, 8, 8]) == 7)

#general case: unsorted list with negative integers (length of list is odd)
def test_upper_quartile_basic4():
    assert(upper_quartile([-12, 5, -22, 30, 7, -36, 14, 42, - 15, 53, 25]) == 30)

#UPPER QUARTILE CORNER CASE:
#corner case: empty list
def test_upper_quartile_corner1():
    assert(upper_quartile([]) == "Error: Empty List")

#corner case: list of 1 integer
def test_upper_quartile_corner2():
    assert(upper_quartile([1]) == "No upper or lower quartile")

#UPPER QUARTILE UNUSUAL CASE:
#unusual case: list with integers and strings
def test_upper_quartile_unusual():
    assert(upper_quartile(["p", "f", 3, "12", "."]) == "Error: TypeError")

#unusual case: list with integers and strings
def test_upper_quartile_unusual2():
    assert(upper_quartile(["good morning", 13, "!?", 7, 3]) == "Error: TypeError")
=======

# GENERAL MEDIAN TESTS
def test_median_basic1():
    assert(median([1, 2, 3, 4, 5, 6, 7]) == 4)

def test_median_basic2():
    assert(median([2, 4, 6, 7]) == 5)

# CORNER MEDIAN TESTS
def test_median_corner1():
    assert(median([]) == "Error: Empty List")

def test_median_corner2():
    assert(median([0]) == 0)

# GENERAL RANGE TESTS
def test_range_basic1():
    assert(ranges([1, 2, 3, 4, 5, 6]) == 5)

def test_range_basic2():
    assert(ranges([3, 4, 5, 5, 6, 7, 13]) == 10)

# CORNER RANGE TESTS
def test_range_corner1():
    assert(ranges([5]) == 5)

def test_range_corner2():
    assert(ranges([]) == "Error: Empty List")

# GENERAL VARIANCE TESTS
def test_variance_basic1():
    assert(variance([10, 20, 30, 40]) == 125)

def test_variance_basic2():
    assert(variance([600, 470, 170, 430, 300]) == 21704)

# CORNER VARIANCE TESTS
def test_variance_corner1():
    assert(variance([1]) == "Error: List must have 2 or more integers")

def test_variance_corner2():
    assert(variance([]) == "Error: Empty List")
    
# UNUSUAL VARIANCE TEST
def test_variance_unusual1():
    assert(variance(["hello", 10, 20, 30]) == "Error: Type Error")

# GENERAL STANDARD DEVIATION TESTS
def test_standard_deviation_basic1():
    assert(standard_deviation([10, 20, 30, 40]) == (math.sqrt(125)))

def test_standard_deviation_basic2():
    assert(standard_deviation([600, 470, 170, 430, 300]) == (math.sqrt(21704)))

# CORNER STANDARD DEVIATION TESTS
def test_standard_deviation_corner1():
    assert(standard_deviation([1]) == "Error: List must have 2 or more integers")

def test_standard_deviatione_corner2():
    assert(standard_deviation([]) == "Error: Empty List")
    
# UNUSUAL STANDARD DEVIATION TEST
def test_standard_deviation_unusual1():
    assert(standard_deviation(["hello", 10, 20, 30]) == "Error: Type Error")
    
>>>>>>> master
