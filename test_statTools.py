import pytest
from statTools import *

def test_mean_basic1():
    assert(mean([4,1,7,2,8]) == 4.4)

def test_mean_basic2():
    assert(mean([7,1,3,0,0,1]) == 2)

def test_mean_basic3():
    assert(mean([]) == 0)

def test_mean_basic4():
    assert(mean([3,1,-4,1,-6,2]) == -0.5)

def test_mean_corner1():
    assert(mean([0]) == 0)