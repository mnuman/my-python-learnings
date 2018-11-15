"""Unit testing module"""
# pylint: disable=C0111,E0401,C0304,C0413
import sys
import os
import pytest
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))
import day10b

def test_list_to_ascii_codes():
    mylist = [1,2,3]
    assert day10b.list_to_ascii_codes(mylist) == [49,44,50,44,51,17, 31, 73, 47, 23]
    assert day10b.list_to_ascii_codes([1]) == [49,17, 31, 73, 47, 23]

def test_xor_block():
    assert day10b.xor_block([65 , 27 , 9 , 1 , 4 , 3 , 40 , 50 , 91 , 7 , 6 , 0 , 2 , 5 , 68 , 22]) == 64

def test_int_to_hex():
    assert day10b.int_to_hex(2) == '02'
    assert day10b.int_to_hex(10) == '0a'
    assert day10b.int_to_hex(255) == 'ff'

def test_sparsify_list_zero_blocksize():
    with pytest.raises(AssertionError):
        day10b.sparsify_list([])

def test_sparsify_list_invalid_blocksize():
    with pytest.raises(AssertionError):
        day10b.sparsify_list([1,2,3,4,5])

def test_sparsify_list_single_block():
    input_list = [65 , 27 , 9 , 1 , 4 , 3 , 40 , 50 , 91 , 7 , 6 , 0 , 2 , 5 , 68 , 22]
    assert day10b.sparsify_list(input_list) == [64]

def  test_sparsify_list_multi_block():
    input_list = [65 , 27 , 9 , 1 , 4 , 3 , 40 , 50 , 91 , 7 , 6 , 0 , 2 , 5 , 68 , 22] * 5
    assert day10b.sparsify_list(input_list) == [64]*5     