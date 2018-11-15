""" Part two: garbage counter.
Now, you're ready to remove the garbage.

To prove you've removed it, you need to count all of the characters within
the garbage. The leading and trailing < and > don't count, nor do any
canceled characters or the ! doing the canceling.

<>, 0 characters.
<random characters>, 17 characters.
<<<<>, 3 characters.
<{!>}>, 2 characters.
<!!>, 0 characters.
<!!!>>, 0 characters.
<{o"i!a,<{i<a>, 10 characters.
"""
import os
def process_stream(line):
    """Process the line, in a character wise fashion using the rules defined above"""
    garbage_counter = 0
    depth = 0
    garbage = False
    ignoreNext = False

    for c in line:
        if garbage:
            if not ignoreNext:
                if c == '>':
                    # garbage ends on >
                    garbage = False
                elif c == '!':
                    # ! makes us ignore the next character in garbage mode
                    ignoreNext = True
                else:
                    garbage_counter += 1
            else:
                # after ignoring the character in garbage mode, the next one should be okay
                ignoreNext = False
        else:
            if c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
            elif c == '<':
                garbage = True

    return garbage_counter

if __name__ == '__main__':
    # read the file, but it is just a single line
    with open(os.path.join(os.path.dirname(__file__), './day9.txt'), 'r') as f:
        lines = f.readlines()
    print (process_stream(lines[0]))
    # 14421
    # 9b: 6817