# pylint: disable=W0621,W0612,C0103,W1401
"""--- Day 8: I Heard You Like Registers ---
You receive a signal directly from the CPU. Because of your recent assistance
with jump instructions, it would like you to compute the result of a series
of unusual register instructions.

Each instruction consists of several parts: the register to modify, whether
to increase or decrease that register's value, the amount by which to increase
or decrease it, and a condition. If the condition fails, skip the instruction
without modifying the register. The registers all start at 0. The instructions
look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
These instructions would be processed as follows:

Because a starts at 0, it is not greater than 1, and so b is not modified.
a is increased by 1 (to 1) because b is less than 5 (it is 0).
c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
c is increased by -20 (to -10) because c is equal to 10.
After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to).
However, the CPU doesn't have the bandwidth to tell you what all the registers
are named, and leaves that to you to determine.

What is the largest value in any register after completing the
instructions in your puzzle input?
"""
import re
import os

def validate_register(registers, register):
    """Validate that the register exists, otherwise initialize it!"""
    if register not in registers:
        registers[register] = 0

class Instruction():
    """Let's build an class to represent the instruction - for getting more
       familiar with classes and simple because it is possible :-)
    """
    def __init__(self, register, opcode, opcode_argument
                 , condition_register, condition_operator, condition_argument):
        self.register = register
        self.opcode = opcode
        self.opcode_argument = int(opcode_argument)
        self.condition_register = condition_register
        self.condition_operator = condition_operator
        self.condition_argument = int(condition_argument)

    def _validate(self, registers):
        validate_register(registers, self.register)
        validate_register(registers, self.condition_register)

    def _buildCondition(self, registers):
        """Build the condition to evaluate"""
        self._validate(registers)
        return str(registers[self.condition_register]) + \
                self.condition_operator + \
                str(self.condition_argument)

    def _translate_opcode(self):
        """Translate opcode to Python expression"""
        if self.opcode == 'inc':
            return ' + '
        elif self.opcode == 'dec':
            return ' - '
        return ' invalid opcode ' + self.opcode

    def _buildOperation(self, registers):
        """Build the operation to execute"""
        self._validate(registers)
        return "registers['" + self.register + "']" + \
                self._translate_opcode() + \
                str(self.opcode_argument)

    def execute(self, registers):
        """Execute this instruction on the set of registers provided"""
        self._validate(registers)
        condition = self._buildCondition(registers)
        # pylint: disable=W0123
        if eval(condition):
            # condition is satisfied, so adjust the register value
            # as the eval just evaluates the expression, re-assign its value
            # to the correct register
            registers[self.register] = eval(self._buildOperation(registers))


def readfile(filename):
    """Read file and return as a list of lines"""
    with open(filename, "r") as the_file:
        lines = the_file.readlines()
    return [l for l in lines]

def parse_data(lines):
    """Process the array of lines into dictionary where every node points to its parent
    instruction format: ssv dec -128 if tlj <= 360
                        rg1 opc  arg if rg2 cmp val
    regex: r'^(\w+) (\w+) ([+\-0-9]+) if (\w+) (\W+) ([+\-0-9]+)$'
    """
    lineregex = re.compile(r'^(\w+) (\w+) ([+\-0-9]+) if (\w+) (\W+) ([+\-0-9]+)$')
    instruction_list = []
    # matches: 0 - node, 1 - weight, 2: list of children
    for line in lines:
        match = lineregex.match(line)
        if match is not None:
            g = match.groups()
            n = Instruction(register=g[0],
                            opcode=g[1],
                            opcode_argument=g[2],
                            condition_register=g[3],
                            condition_operator=g[4],
                            condition_argument=g[5]
                            )
            instruction_list.append(n)
    return instruction_list

def execute_all(registers, instructions):
    """Process all instructions in list order"""
    max_val = 0
    for instruction in instructions:
        instruction.execute(registers)
        max_val = max(max_val, retrieve_max_register(registers))
    return max_val

def retrieve_max_register(registers):
    return max(registers.values())

if __name__ == '__main__':
    registers = {}
    lines = readfile(os.path.join(os.path.dirname(__file__), 'day8.txt'))
    instructions = parse_data(lines)
    assert len(instructions) == 1000
    print(execute_all(registers, instructions))
    # print(retrieve_max_register(registers))
    # 8: 5102
    # 8b: 6056

