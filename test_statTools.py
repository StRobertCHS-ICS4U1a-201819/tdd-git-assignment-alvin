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


