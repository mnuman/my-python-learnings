import os
def readfile(filename):
    with open(filename,"r") as f:
        lines =  f.readlines()
    return lines

def word_aggregator(line):
    """The result for the line is a LIST containing all the word's fingerprints
       A fingerprint is a sorted concatenation of letters and their number of occurrences,
       e.g. aap --> a2p1
    """ 
    res = []
    for word in line.split():
        word_fingerprint = ''
        chars = {}
        for c in word:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
        for k in sorted(chars):
            word_fingerprint = word_fingerprint + k + str(chars[k])
        res.append(word_fingerprint)
    return res

def is_okay(list_word_fingerprints):
    # no permutations if the list has only unique word fingerprints for the line
    return len(list_word_fingerprints) == len(set(list_word_fingerprints))

if __name__ == '__main__':
    cnt = 0
    lines = readfile(os.path.join(os.path.dirname(__file__), 'day4.txt'))
    for l in lines:
        if is_okay(word_aggregator(l)):
            cnt += 1
    print(f'Result: {cnt}')
    