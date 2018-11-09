"""Unit testing module"""
# pylint: disable=C0111,E0401,C0304,C0413
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))
import day10

def test_knot_complete():
    s = ['0','1','2','3','4','5','6','7','8','9']
    assert day10.knot(s,0,10) == ['9','8','7','6','5','4','3','2','1','0']

def test_knot_firsthalf():
    s = ['0','1','2','3','4','5','6','7','8','9']
    assert day10.knot(s,0,5) == ['4','3','2','1','0','5','6','7','8','9']

def test_knot_single_element():
    s = ['0','1','2','3','4','5','6','7','8','9']
    assert day10.knot(s,0,1) == ['0','1','2','3','4','5','6','7','8','9']

def test_knot_two_elements():
    s = ['0','1','2','3','4','5','6','7','8','9']
    assert day10.knot(s,0,2) == ['1','0','2','3','4','5','6','7','8','9']

def test_knot_length_0():
    s = ['0','1','2','3','4','5','6','7','8','9']
    assert day10.knot(s,0,0) == ['0','1','2','3','4','5','6','7','8','9']

def test_knot_wrap_around():
    s = ['0','1','2','3','4','5','6','7','8','9']
    assert day10.knot(s,9,2) == ['9','1','2','3','4','5','6','7','8','0']

def test_knot_wrap_around_more():
    s = ['0','1','2','3','4','5','6','7','8','9']
    assert day10.knot(s,5,10) == ['9','8','7','6','5','4','3','2','1','0']

def test_no_jump_no_skip():
    assert day10.new_pos(0,0,0,10) == 0

def test_jump_no_skip():
    assert day10.new_pos(0,3,0,10) == 3

def test_no_jump_skip():
    assert day10.new_pos(0,0,4,10) == 4

def test_jump_skip():
    assert day10.new_pos(0,3,4,10) == 7

def test_jump_skip_wrap():
    assert day10.new_pos(0,5,6,10) == 1

def test_process_all():
     input_list = [0, 1, 2, 3, 4]
     string_lengths = [ 3, 4, 1, 5]
     assert day10.process_all(input_list, string_lengths) == [3, 4, 2, 1, 0]