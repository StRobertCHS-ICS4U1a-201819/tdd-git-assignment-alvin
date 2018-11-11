import pytest
from statTools import*

def test_median_basic1():
    assert(median([1, 2, 3, 4, 5, 6, 7]) == 4)

def test_median_basic2():
    assert(median([9, 8, 7, 6, 5, 4, 3]) == 6)
