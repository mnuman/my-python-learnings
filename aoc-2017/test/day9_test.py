
"""Unit testing module"""
# pylint: disable=C0111,E0401,C0304,C0413
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))
import day9

""" Examples 
{}, score of 1.
{{{}}}, score of 1 + 2 + 3 = 6.
{{},{}}, score of 1 + 2 + 2 = 5.
{{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
{<a>,<a>,<a>,<a>}, score of 1.
{{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.
"""


def test_single_group():
    teststring = '{}'
    assert day9.process_stream(teststring) == 1


def test_nested_groups():
    teststring = '{{{}}}'
    assert day9.process_stream(teststring) == 6

def test_multiple_nested_groups():
    teststring = '{{},{}}'
    assert day9.process_stream(teststring) == 5

def test_multiple_nested_groups2():
    teststring = '{{{},{},{{}}}}'
    assert day9.process_stream(teststring) == 16  

def test_simple_garbage():
    teststring = '{<a>,<a>,<a>,<a>}'
    assert day9.process_stream(teststring) == 1

def test_nested_garbage():
    teststring = '{{<ab>},{<ab>},{<ab>},{<ab>}}'
    assert day9.process_stream(teststring) == 9

def test_nested_garbage_ignores():
    teststring = '{{<!!>},{<!!>},{<!!>},{<!!>}}'
    assert day9.process_stream(teststring) == 9

def test_one_nested_garbage():
    teststring = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
    assert day9.process_stream(teststring) == 3