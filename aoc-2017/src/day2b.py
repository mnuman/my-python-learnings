""" 
"Based on what we're seeing, it looks like all the User wanted is some information about the evenly 
divisible values in the spreadsheet. Unfortunately, none of us are equipped for that kind of calculation -
 most of us specialize in bitwise operations."

It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - 
that is, where the result of the division operation is a whole number. They would like you to find 
those numbers on each line, divide them, and add up each line's result
"""
import os

def readfile(filename):
    with open(filename,"r") as f:
        lines = f.readlines()
    [ l.split() for l in lines ]
    res = []
    for l in lines:
        row = []
        for c in l.split():
            row.append(int(c))
        res.append(row)
    return res

def calc_checksum( matrix):
    res = 0
    for row in matrix:
        for pos, i in enumerate(row[:-1]):
            for j in row[pos+1:]:
                if i > j:
                    if i % j == 0:
                        res += i // j
                else:
                    if j % i == 0:
                        res += j // i
    return res

if __name__ == '__main__':
    data = readfile(os.path.join(os.path.dirname(__file__), 'day2b.txt'))
    result = calc_checksum(data)
    print(f"Solution to the question is {result}")