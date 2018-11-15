import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))

import day3b

def test_getval():
    array = [[1,2,3], [4,5,6], [7,8,None]]
    assert day3b.getval(array,0,0) == 1
    assert day3b.getval(array,2,2) == 0
    assert day3b.getval(array,1,0) == 4

def test_calc_value():
    none_array = [[None,None,None],[None,None,None],[None,None,None]]
    assert day3b.calc_value(none_array,1,1) == 1
    
    array = [[1,2,3], [4,5,6], [7,8,None]]
    assert day3b.calc_value(array,1,1) == 31

def test_adjacent_sum():
    # first element exceeding 9 in 5x5 square is 10 (row=2,col=1)
    assert day3b.adjacent_sum(5,9) == 10
    assert day3b.adjacent_sum(7,351) == 362