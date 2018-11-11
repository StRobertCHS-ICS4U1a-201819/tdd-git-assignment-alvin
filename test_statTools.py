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

#general case: sorted list
def test_mode_basic1():
    assert(mode([1,2,2,4,5,7,8]) == 2)

#general case: unsorted list
def test_mode_basic2():
    assert(mode([5,1,2,7,2,8,4]) == 2)

#general case: list with negative integers included
def test_mode_basic3():
    assert(mode([1,4,3,-5,-1,4,2]) == 4)

#general case: more than one mode
def test_mode_basic4():
    assert(mode([1, 3, 2, 3, 1, 4, 4, 5]) == "There is no unique mode")

#corner case: empty list
def test_mode_corner():
    assert(mode([]) == "empty string list")

#corner case: list of one integer
def test_mode_corner2():
    assert(mode([1]) == 1)

#unusual case: list with integers and strings
def test_mode_unusual():
    assert(mode(["3", "1", "5", 1, "7", 3]) == "There is no unique mode")

#unusual case: list with integers and strings
def test_mode_unusual2():
    assert (mode(["3", "f", 7, ".","r", "g", 3, "."]) == ".")






