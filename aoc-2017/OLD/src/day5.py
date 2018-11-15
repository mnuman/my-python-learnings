import os
"""Day 5 - Advent of Code

An urgent interrupt arrives from the CPU: it's trapped in a maze of jump
instructions, and it would like assistance from any programs with spare
cycles to help find the exit.

The message includes a list of the offsets for each jump. Jumps are relative:
 -1 moves to the previous instruction, and 2 skips the next one. Start at
 the first instruction in the list. The goal is to follow the jumps until
 one leads outside the list.

In addition, these instructions are a little strange; after each jump,
the offset of that instruction increases by 1. So, if you come across
an offset of 3, you would move three instructions forward, but change
it to a 4 for the next time it is encountered.

For example, consider the following list of jump offsets:

0
3
0
1
-3
Positive jumps ("forward") move downward; negative jumps move upward. For
legibility in this example, these offset values will be written all on
one line, with the current instruction marked in parentheses. The
following steps would be taken before an exit is found:

(0) 3  0  1  -3  - before we have taken any steps.
(1) 3  0  1  -3  - jump with offset 0 (that is, don't jump at all).
                   Fortunately, the instruction is then incremented to 1.
 2 (3) 0  1  -3  - step forward because of the instruction we just modified.
                   The first instruction is incremented again, now to 2.
 2  4  0  1 (-3) - jump all the way to the end; leave a 4 behind.
 2 (4) 0  1  -2  - go back to where we just were; increment -3 to -2.
 2  5  0  1  -2  - jump 4 steps forward, escaping the maze.
In this example, the exit is reached in 5 steps.

How many steps does it take to reach the exit?
"""
def readfile(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    res = []
    for l in lines:
        res.append(int(l))
    return res

def jumps(offsets):
    """Perform jumps using the jump offset at the specified positions.
       Pass in offset as list of integers.
    """

    jumpcounter = 0
    position = 0
    while position < len(offsets) and position >= 0:
        newposition = position + offsets[position]
        offsets[position] += 1
        jumpcounter += 1
        #print(f"Current position: {position}, newposition: {newposition}"
        #      f", jumpcounter: {jumpcounter}")
        # print(offsets)
        position = newposition
    return jumpcounter

def jumps5b(offsets):
    """Perform jumps using the jump offset at the specified positions.
       Pass in offset as list of integers.
    """

    jumpcounter = 0
    position = 0
    while position < len(offsets) and position >= 0:
        newposition = position + offsets[position]
        """Now, the jumps are even stranger: after each jump, if the offset
           was three or more, instead decrease it by 1. Otherwise, increase
           it by 1 as before.
        """
        if offsets[position] >= 3:
            offsets[position] -= 1
        else:
            offsets[position] += 1

        jumpcounter += 1
        #print(f"Current position: {position}, newposition: {newposition}"
        #      f", jumpcounter: {jumpcounter}")
        # print(offsets)
        position = newposition
    return jumpcounter

if __name__ == '__main__':
    data = readfile(os.path.join(os.path.dirname(__file__), 'day5.txt'))
    result = jumps5b(data)
    print(f"Solution to the question is {result}")
    #5: 358131
