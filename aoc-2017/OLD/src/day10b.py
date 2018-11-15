# pylint: disable=W0621,W0612,C0103,W1401
"""The logic you've constructed forms a single round of the Knot Hash 
algorithm; running the full thing requires many of these rounds. Some 
input and output processing is also required.

First, from now on, your input should be taken not as a list of numbers, 
but as a string of bytes instead. Unless otherwise specified, convert 
characters to bytes using their ASCII codes. This will allow you to 
handle arbitrary ASCII strings, and it also ensures that your input 
lengths are never larger than 255. For example, if you are given 1,2,3, 
you should convert it to the ASCII codes for each character: 49,44,50,44,51.

Once you have determined the sequence of lengths to use, add the following 
lengths to the end of the sequence: 17, 31, 73, 47, 23. For example, 
if you are given 1,2,3, your final sequence of lengths should be 
49,44,50,44,51,17,31,73,47,23 (the ASCII codes from the input string 
combined with the standard length suffix values).

Second, instead of merely running one round like you did above, 
run a total of 64 rounds, using the same length sequence in each round. 
The current position and skip size should be preserved between rounds. 
For example, if the previous example was your first round, you would 
start your second round with the same length sequence 
(3, 4, 1, 5, 17, 31, 73, 47, 23, now assuming they came 
from ASCII codes and include the suffix), but start with the 
previous round's current position (4) and skip size (4).

Once the rounds are complete, you will be left with the numbers 
from 0 to 255 in some order, called the sparse hash. Your next task 
is to reduce these to a list of only 16 numbers called the dense hash. 
To do this, use numeric bitwise XOR to combine each consecutive block 
of 16 numbers in the sparse hash (there are 16 such blocks in a list of 
256 numbers). So, the first element in the dense hash is the first 
sixteen elements of the sparse hash XOR'd together, the second element 
in the dense hash is the second sixteen elements of the sparse hash XOR'd 
together, etc.

For example, if the first sixteen elements of your sparse hash are as 
shown below, and the XOR operator is ^, you would calculate the first 
output number like this:

65 ^ 27 ^ 9 ^ 1 ^ 4 ^ 3 ^ 40 ^ 50 ^ 91 ^ 7 ^ 6 ^ 0 ^ 2 ^ 5 ^ 68 ^ 22 = 64
Perform this operation on each of the sixteen blocks of sixteen numbers 
in your sparse hash to determine the sixteen numbers in your dense hash.

Finally, the standard way to represent a Knot Hash is as a single 
hexadecimal string; the final output is the dense hash in hexadecimal 
notation. Because each number in your dense hash will be between 
0 and 255 (inclusive), always represent each number as two hexadecimal 
digits (including a leading zero as necessary). So, if your first 
three numbers are 64, 7, 255, they correspond to the hexadecimal numbers 
40, 07, ff, and so the first six characters of the hash would be 4007ff. 
Because every Knot Hash is sixteen such numbers, the hexadecimal 
representation is always 32 hexadecimal digits (0-f) long.

Here are some example hashes:

The empty string becomes a2582a3a0e66e6e86e3812dcb672a272.
AoC 2017 becomes 33efeb34ea91902bb2f59c9920caa6cd.
1,2,3 becomes 3efbe78a8d82f29979031a4aa0b16a9d.
1,2,4 becomes 63960835bcdc130f0b66d7ff4f6a5a8e.
Treating your puzzle input as a string of ASCII characters, what 
is the Knot Hash of your puzzle input? Ignore any leading or trailing 
whitespace you might encounter.
"""
def cycle2(string, startpos, skip, length):
    """Perform one cycle, from the current startposition"""
    l = len(string)
    if startpos + length < l:
        s = string[startpos:startpos + length]
    else:
        s = string[startpos:] + string[:startpos + length - l]
    return s


def knot(inputlist, startpos, length):
    lengte_inputlist = len(inputlist)
    sublist_to_process = []
    pos = startpos

    cnt = 0
    while cnt < length:
        sublist_to_process.append(inputlist[pos])
        cnt += 1
        pos = (pos + 1) % (lengte_inputlist)

    sublist_to_process.reverse()

    pos = startpos
    for c in sublist_to_process:
        inputlist[pos] = c
        pos = (pos + 1) % (lengte_inputlist)
    return inputlist

def new_pos(current, move, skip, length):
    """Determine new position, starting from current, 
       moving 'move' elements and skipping 'skip' elements.
       Wrap around by applying length criterion
    """
    return (current + move + skip) % length

def process_all(input_list, input_lengths):
    """Process the characters in the input_list using the 
       input_lengths according to the given algorithm"""
    skip = 0
    pos  = 0
    length = len(input_list)
    for r in range(0,64):
        for ipl in input_lengths:
            knot(input_list, pos, ipl)
            pos = new_pos(pos, ipl, skip, length)
            skip = (skip + 1 ) % length
    return input_list

def xor_block(sixteen_bytes):
    """Calculate the xor product for the sixteen numbers in the list provided"""
    assert len(sixteen_bytes) == 16
    result = 0
    for n in sixteen_bytes:
        result = result ^ n
    return result

def list_to_ascii_codes(list):
    return [ ord(c) for c in ','.join(str(n) for n in list) ]  + [17, 31, 73, 47, 23]

def int_to_hex(value):
    return f"{value:0{2}x}"

def sparsify_list(multi16_list):
    assert len(multi16_list) > 0 and len(multi16_list) % 16 == 0
    dense_hash = []
    for i in range(0, len(multi16_list)//16):
        block_of_16 = multi16_list[i*16:16*(i+1)]
        dense_hash.append(xor_block( block_of_16))
    return dense_hash

if __name__ == '__main__':
    input_list = [x for x in range(0,256)]
    # lengths = list_to_ascii_codes([106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36])
    lengths = [1,2,3]
    output_list = process_all(input_list, lengths)
    print(output_list)
    print([int_to_hex(c) for c in sparsify_list(output_list)])