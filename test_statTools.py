import pytest
from statTools import *

def test_mean_basic1():
    assert(mean([4,1,7,2,8]) == 4.4)