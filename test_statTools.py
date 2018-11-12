<<<<<<< HEAD
"""
-------------------------------------------------------------------------------
Name:		test_statTools.py
Purpose:
Tests for all functions through pytest

Author:		Ru. E

Created:	11/11/2018
------------------------------------------------------------------------------
"""


import pytest
from statTools import*


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
=======
import pytest
from statTools import*
>>>>>>> master

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
