import pytest
from statTools import *

def test_mean_basic1():
    assert(mean([4,1,7,2,8]) == 4.4)

def test_mean_basic2():
    assert(mean([7,1,3,0,0,1]) == 2)
