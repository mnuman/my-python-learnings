"""Unit testing module"""
# pylint: disable=C0111,E0401,C0304,C0413
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))

import day8

def test_parse():
    """Count instructions and test parser"""
    lines = day8.readfile(os.path.join(os.path.dirname(__file__), 'day8a.txt'))
    instructions = day8.parse_data(lines)
    assert len(instructions) == len(lines)
    assert instructions[0].register == 'smi'
    assert instructions[0].opcode == 'inc'
    assert instructions[0].opcode_argument == 781
    assert instructions[0].condition_register == 'epx'
    assert instructions[0].condition_operator == '>'
    assert instructions[0].condition_argument == -2
    # last instructiuon
    assert instructions[5].register == 'vlh'

def test__validate():
    registers = {}
    instruction = day8.Instruction('aap', 'inc', '12', 'noot', '==', '14')
    # pylint: disable=W0212
    instruction._validate(registers)
    assert len(registers) == 2
    assert 'aap' in registers
    assert 'noot' in registers

def test_build_condition():
    registers = {}
    instruction = day8.Instruction('aap', 'inc', '12', 'noot', '==', '14')
    # pylint: disable=W0212
    condition = instruction._buildCondition(registers)
    assert condition == '0==14'
    # pylint: disable=W0123
    assert not eval(condition)

def test_build_operation():
    registers = {}
    instruction = day8.Instruction('aap', 'inc', '12', 'noot', '==', '14')
    # pylint: disable=W0212
    operation = instruction._buildOperation(registers)
    assert operation == "registers['aap'] + 12"
    assert len(registers) == 2 # implicit validation

def test_execute_operation():
    registers = {}
    instruction = day8.Instruction('aap', 'inc', '12', 'noot', '!=', '14')
    instruction.execute(registers)
    assert len(registers) == 2
    assert 'aap' in registers and registers['aap'] == 12
    assert 'noot' in registers and registers['noot'] == 0

def test_execute_all():
    registers = {}
    lines = day8.readfile(os.path.join(os.path.dirname(__file__), 'day8a.txt'))
    instructions = day8.parse_data(lines)
    day8.execute_all(registers, instructions)
    assert len(registers) == 10
    assert 'smi' in registers and registers['smi'] == 781
    assert 'tlj' in registers and registers['tlj'] == 356

def test_max_value():
    registers = { 'a' : 1, 'b': -15, 'c' : 42, 'd': -908, 'e': 42 }
    assert day8.retrieve_max_register(registers) == 42
