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
        res += (max(row)-min(row))
    return res

if __name__ == '__main__':
    data = readfile(os.path.join(os.path.dirname(__file__), 'day2a.txt'))
    result = calc_checksum(data)
    print(f"Solution to the question is {result}")
