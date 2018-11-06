"""Unit testing module"""
# pylint: disable=C0111,E0401,C0304,C0413
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))

import day6

def test_memorybanks():
    memorybanks = [0, 3, 0, 1, 2]
    assert day6.max_bank(memorybanks) == (1, 3)

def test_memorybanks_end():
    memorybanks = [-12, 3, 0, 1, 9]
    assert day6.max_bank(memorybanks) == (4, 9)

def test_memorybanks_first_max():
    memorybanks = [0, 3, 9, 1, 9]
    assert day6.max_bank(memorybanks) == (2, 9)

def test_cycle_banks_noop():
    memorybanks = [0, 3, 9, 1, 9]
    assert day6.cycle_banks(memorybanks, 0) == [0, 3, 9, 1, 9]

def test_cycle_banks_single():
    memorybanks = [0, 3, 9, 1, 9]
    assert day6.cycle_banks(memorybanks, 3) == [0, 3, 9, 0, 10]

def test_cycle_banks_simple():
    memorybanks = [0, 3, 9, 1, 9]
    assert day6.cycle_banks(memorybanks, 4) == [2, 5, 11, 3, 1]

def test_known_states_dupe():
    day6.reset_known_states()
    memorybanks = [0, 3, 9, 1, 9]
    assert not day6.known_state(memorybanks)   # unknowsn, register
    assert day6.known_state(memorybanks)       # known now!

def test_known_states_multiple():
    day6.reset_known_states()
    memorybanks = [0, 3, 9, 1, 9]
    assert not day6.known_state(memorybanks)   # unknown, register
    memorybanks = [0, 3, 9, 0, 10]
    assert not day6.known_state(memorybanks)   # unknown, register
    assert day6.known_state(memorybanks)
    memorybanks = [0, 3, 9, 1, 9]
    assert day6.known_state(memorybanks)

def test_reallocate_memory_noop():
    day6.reset_known_states()
    memorybanks = [0, 0, 0]
    assert day6.reallocate_memory(memorybanks) == 1

def test_reallocate_memory_one():
    day6.reset_known_states()
    memorybanks = [0, 0, 1]
    #  001 --> 100 --> 010 --> 001
    assert day6.reallocate_memory(memorybanks) == 3

def test_reallocate_memory_simple():
    day6.reset_known_states()
    memorybanks = [0, 0, 3]
    # 0 0 3 --> 1 1 1 --> 0 2 1 --> 1 0 2 --> 2 1 0 --> 0 2 1
    assert day6.reallocate_memory(memorybanks) == 5

def test_reallocate_memory_example():
    day6.reset_known_states()
    memorybanks = [0, 2, 7, 0]
    assert day6.reallocate_memory(memorybanks) == 5

def test_reallocate_memory_simple_v2():
    day6.reset_known_states()
    memorybanks = [0, 0, 3]
    # 0: 0 0 3 --> 1: 1 1 1 --> 2: 0 2 1 --> 3: 1 0 2 --> 4: 2 1 0 --> 5: 0 2 1
    assert day6.reallocate_memory_with_counter(memorybanks) == 5 - 2
