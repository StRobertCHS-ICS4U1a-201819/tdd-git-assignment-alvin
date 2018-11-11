import pytest
from statTools import*

# MEDIAN TESTS
def test_median_basic1():
    assert(median([1, 2, 3, 4, 5, 6, 7]) == 4)

def test_median_basic2():
    assert(median([9, 8, 7, 6, 5, 4, 3]) == 6)

def test_median_basic3():
    assert(median([2, 4, 6, 7]) == 5)

def test_median_basic4():
    assert(median([]) == 0)

# RANGE TESTS
def test_range_basic1():
    assert(range([1, 2, 3, 4, 5]) == 4)

def test_range_basic2():
    assert(range([3, 4, 5, 5, 6, 7, 13]) == 10)

def test_range_basic3():
    assert(range([5]) == 5)

def test_range_basic4():
    assert(range([]) == 0)

# VARIANCE TESTS

