"""Unit testing module"""
# pylint: disable=C0111,E0401,C0304,C0413
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))

import day7

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

def test_all_lines_converted():
    lines = day7.readfile(os.path.join(os.path.dirname(__file__), 'day7a.txt'))
    all_me_nodes = day7.parse_data_7b(lines)
    assert len(all_me_nodes) == len(lines)
    assert ('gyxo' in all_me_nodes and
            all_me_nodes['gyxo'].name == 'gyxo' and
            all_me_nodes['gyxo'].weight == 61 and
            all_me_nodes['gyxo'].parent is None and
            all_me_nodes['gyxo'].subtreeweight is None and
            all_me_nodes['gyxo'].children == [])
    assert ('fwft' in all_me_nodes and
            all_me_nodes['fwft'].weight == 72 and
            isinstance(all_me_nodes['fwft'].children, list) and
            'ktlj' in all_me_nodes['fwft'].children and
            len(all_me_nodes['fwft'].children) == 3)


def test_tree():
    lines = day7.readfile(os.path.join(os.path.dirname(__file__), 'day7a.txt'))
    all_nodes = day7.parse_data_7b(lines)
    all_nodes = day7.build_tree(all_nodes)
    assert len(all_nodes) == len(lines)
    assert 'gyxo' in all_nodes
    assert all_nodes['gyxo'].parent.name == 'ugml'

def test_find_tree_root():
    lines = day7.readfile(os.path.join(os.path.dirname(__file__), 'day7a.txt'))
    all_nodes = day7.parse_data_7b(lines)
    all_nodes = day7.build_tree(all_nodes)
    root = day7.find_tree_root(all_nodes)
    assert root is not None
    assert root.name == 'tknk'

def test_weight_leaf():
    lines = day7.readfile(os.path.join(os.path.dirname(__file__), 'day7a.txt'))
    all_nodes = day7.parse_data_7b(lines)
    all_nodes = day7.build_tree(all_nodes)
    day7.weigh_subtree(all_nodes, all_nodes['gyxo'])
    assert all_nodes['gyxo'].subtreeweight == 61

def test_weighed_tree():
    lines = day7.readfile(os.path.join(os.path.dirname(__file__), 'day7a.txt'))
    all_nodes = day7.parse_data_7b(lines)
    all_nodes = day7.build_tree(all_nodes)
    all_nodes = day7.weighted_tree(all_nodes)
    assert 'gyxo' in all_nodes and all_nodes['gyxo'].subtreeweight == 61
    assert 'ugml' in all_nodes and all_nodes['ugml'].subtreeweight == 251
    assert 'padx' in all_nodes and all_nodes['padx'].subtreeweight == 243
    assert 'fwft' in all_nodes and all_nodes['fwft'].subtreeweight == 243
    assert 'tknk' in all_nodes and all_nodes['tknk'].subtreeweight == sum(all_nodes[n].weight for n in all_nodes)

def test_unbalanced_node():
    lines = day7.readfile(os.path.join(os.path.dirname(__file__), 'day7a.txt'))
    all_nodes = day7.parse_data_7b(lines)
    assert day7.find_unbalanced_node(all_nodes) == ('ugml', 251, 243, 60)
