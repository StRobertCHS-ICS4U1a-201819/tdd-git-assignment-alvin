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
def test_ranges_basic1():
    assert(range([1, 2, 3, 4, 5, 6]) == 5)

def test_ranges_basic2():
    assert(range([3, 4, 5, 5, 6, 7, 13]) == 10)

# CORNER RANGE TESTS
def test_ranges_corner1():
    assert(range([5]) == 5)

def test_ranges_corner2():
    assert(range([]) == "Error: Empty List")

# GENERAL VARIANCE TESTS
def test_variance_basic1():
    assert()


