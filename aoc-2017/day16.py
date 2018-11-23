"""
--- Day 16: Permutation Promenade ---
You come upon a very unusual sight; a group of programs here appear to be dancing.

There are sixteen programs in total, named a through p. They start by standing in a line: a stands in position 0, b stands in position 1, and so on until p, which stands in position 15.

The programs' dance consists of a sequence of dance moves:

Spin, written sX, makes X programs move from the end to the front, but maintain their order otherwise. (For example, s3 on abcde produces cdeab).
Exchange, written xA/B, makes the programs at positions A and B swap places.
Partner, written pA/B, makes the programs named A and B swap places.
For example, with only five programs standing in a line (abcde), they could do the following dance:

s1, a spin of size 1: eabcd.
x3/4, swapping the last two programs: eabdc.
pe/b, swapping programs e and b: baedc.
After finishing their dance, the programs end up in order baedc.

You watch the dance for a while and record their dance moves (your puzzle input). In what order are the programs standing after their dance?
"""


def spin(sequence, size):
    ls = len(sequence)
    s = -(size % ls)
    if s != 0:
        return sequence[s:] + sequence[:s]
    else:
        return sequence


def exchange(string, a, b):
    sequence = [c for c in string]
    if a >= 0 and b >= 0 and a < len(sequence) and b < len(sequence):
        sequence[a], sequence[b] = sequence[b], sequence[a]
    return ''.join(sequence)


def partner(string, a, b):
    sequence = [c for c in string]
    if a in sequence and b in sequence:
        posa = sequence.index(a)
        posb = sequence.index(b)
        sequence[posa], sequence[posb] = sequence[posb], sequence[posa]
    return ''.join(sequence)


def readfile(fname):
    """Read the instructions file and return as a list of instructions"""
    with open(fname) as f:  # pylint: disable=C0103
        content = f.readlines()
    return content[0].split(',')


def perform_ops(seq, operations):
    """Apply the operation in the list iteratively to the seq, return the final result"""
    for op in operations:
        if op[0] == 's':
            opcode = op[1:]
            seq = spin(seq, int(opcode))
        elif op[0] == 'p':
            opcode1, opcode2 = op[1:].split('/')
            seq = partner(seq, opcode1, opcode2)
        elif op[0] == 'x':
            opcode1, opcode2 = op[1:].split('/')
            seq = exchange(seq, int(opcode1), int(opcode2))
        else:
            pass
    return seq


if __name__ == '__main__':
    # seq = 'abcdefghijklmnop'
    # ops = readfile('day16_input.txt')
    # result = perform_ops(seq, ops)
    # print(result)
    # padheomkgjfnblic
