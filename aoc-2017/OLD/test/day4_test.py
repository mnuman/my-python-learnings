import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))

import day4

def test_word_aggregator():
    line = 'aa bb aa'
    assert day4.word_aggregator(line) == { 'aa' : 2, 'bb' : 1}

def test_is_value():
    assert day4.is_valid({ 'aa' : 1, 'bb' : 1})
    assert not(day4.is_valid({ 'aa' : 2, 'bb' : 1}))