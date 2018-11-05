"""Unit testing module"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))

import day5

def test_jumpertje():
    JLIST = [0, 3, 0, 1, -3]
    assert day5.jumps(JLIST) == 5

def test_jumpertje_5b():
    JLIST = [0, 3, 0, 1, -3]
    assert day5.jumps5b(JLIST) == 10
