import pytest
from statTools import *

#general case: sorted list
def test_mean_basic1():
    assert(mean([1,2,4,7,8]) == 4.4)

#general case: unsorted list
def test_mean_basic2():
    assert(mean([7,1,3,0,0,1]) == 2)

#general case: list with negative integers included
def test_mean_basic3():
    assert(mean([3,1,-4,1,-6,2]) == -0.5)

#corner case: list of 1 integer
def test_mean_corner1():
    assert(mean([0]) == 0)

#corner case: empty list
def test_mean_corner2():
    assert(mean([]) == "Error: Empty List")

#unusual case: string input
def test_mean_unusual():
    assert(mean(["2","4","7","3"]) == "Error: TypeError")

