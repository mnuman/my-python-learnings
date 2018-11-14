
"""Unit testing module"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))
import day12

def test_read_file():
    nodes = day12.readfile(os.path.join(os.path.dirname(__file__), 'day12.txt'))
    assert len(nodes) == 7
    assert nodes['6'] == ['4','5']

def test_reachable():
    nodes = day12.readfile(os.path.join(os.path.dirname(__file__), 'day12.txt'))
    reachable_nodes = day12.reachable(nodes,'0')
    assert len(reachable_nodes) == 6
    assert sorted(reachable_nodes) == sorted(['0','2','3','4','5','6'])

def test_reachable_just_self():
    nodes = day12.readfile(os.path.join(os.path.dirname(__file__), 'day12.txt'))
    reachable_nodes = day12.reachable(nodes,'1')
    assert len(reachable_nodes) == 1
    assert reachable_nodes == ['1']
