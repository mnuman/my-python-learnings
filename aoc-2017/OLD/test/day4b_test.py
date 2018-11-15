import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))

import day4b

def test_word_aggregator():
    line = 'aa bb aa'
    assert day4b.word_aggregator(line) == ['a2', 'b2', 'a2']
    line = 'aap noot mies'
    assert day4b.word_aggregator(line) == ['a2p1', 'n1o2t1', 'e1i1m1s1']

def test_is_okay():
    assert not day4b.is_okay(['a2', 'b2', 'a2'])
    assert day4b.is_okay(['a2p1', 'n1o2t1', 'e1i1m1s1'])
