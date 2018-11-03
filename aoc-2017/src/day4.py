import os
def readfile(filename):
    with open(filename,"r") as f:
        lines =  f.readlines()
    return lines

def word_aggregator(line):
    res = {}
    for word in line.split():
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    return res

# Simply iterate over all values and return True if all are 1
def is_valid(dict):
    for key in dict:
        if dict[key] != 1:
            return False
    return True

if __name__ == '__main__':
    cnt = 0
    lines = readfile(os.path.join(os.path.dirname(__file__), 'day4.txt'))
    for l in lines:
        if is_valid(word_aggregator(l)):
            cnt += 1
    print(f'Result: {cnt}')
    