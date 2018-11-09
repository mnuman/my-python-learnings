
"""Unit testing module"""
# pylint: disable=C0111,E0401,C0304,C0413
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))
import day9b

""" 
<>, 0 characters.
<random characters>, 17 characters.
<<<<>, 3 characters.
<{!>}>, 2 characters.
<!!>, 0 characters.
<!!!>>, 0 characters.
<{o"i!a,<{i<a>, 10 characters.
"""


def test_single_group():
    teststring = '<>'
    assert day9b.process_stream(teststring) == 0

def test_long_garbage():
    teststring = '<random characters>'
    assert day9b.process_stream(teststring) == 17

def test_multi_less():
    teststring = '<<<<>'
    assert day9b.process_stream(teststring) == 3

def test_ignore():
    teststring = '<{!>}>'
    assert day9b.process_stream(teststring) == 2

def test_ignore_ignore():
    teststring = '!!>'
    assert day9b.process_stream(teststring) == 0

def test_ignore_terminator():
    teststring = '<!!!>>'
    assert day9b.process_stream(teststring) == 0

def test_misc_garbage():
    teststring = '<{o"i!a,<{i<a>'
    assert day9b.process_stream(teststring) == 10
