"""Unit testing module"""
# pylint: disable=C0111,E0401,C0304,C0413
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))

import day7
import generic

def test_parse():
    lines = day7.readfile(os.path.join(os.path.dirname(__file__), 'day7a.txt'))
    parents = day7.parse_data_7(lines)
    assert parents['xhth'] == 'fwft'
    assert parents['fwft'] == 'tknk'
    assert 'tknk' not in parents

def test_find_root():
    lines = day7.readfile(os.path.join(os.path.dirname(__file__), 'day7a.txt'))
    parents = day7.parse_data_7(lines)
    root = day7.find_root(parents)
    assert root == 'tknk'
