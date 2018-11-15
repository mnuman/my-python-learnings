# pylint: disable=W0621,W0612,C0103
"""
--- Day 6: Memory Reallocation ---
A debugger program here is having an issue: it is trying to repair a memory
reallocation routine, but it keeps getting stuck in an infinite loop.

In this area, there are sixteen memory banks; each memory bank can hold
any number of blocks. The goal of the reallocation routine is to balance
the blocks between the memory banks.

The reallocation routine operates in cycles. In each cycle, it finds
the memory bank with the most blocks (ties won by the lowest-numbered
memory bank) and redistributes those blocks among the banks. To do this,
it removes all of the blocks from the selected bank, then moves to the
next (by index) memory bank and inserts one of the blocks. It continues
doing this until it runs out of blocks; if it reaches the last memory bank,
it wraps around to the first one.

The debugger would like to know how many redistributions can be done before
a blocks-in-banks configuration is produced that has been seen before.

For example, imagine a scenario with only four memory banks:

The banks start with 0, 2, 7, and 0 blocks. The third bank has the most
blocks, so it is chosen for redistribution.
Starting with the next bank (the fourth bank) and then continuing to the
first bank, the second bank, and so on, the 7 blocks are spread out over
the memory banks. The fourth, first, and second banks get two blocks each,
and the third bank gets one back. The final result looks like this: 2 4 1 2.
Next, the second bank is chosen because it contains the most blocks (four).
Because there are four memory banks, each gets one block.
The result is: 3 1 2 3.
Now, there is a tie between the first and fourth memory banks, both
of which have three blocks. The first bank wins the tie, and its three
blocks are distributed evenly over the other three banks, leaving it
with none: 0 2 3 4.
The fourth bank is chosen, and its four blocks are distributed such
that each of the four banks receives one: 1 3 4 1.
The third bank is chosen, and the same thing happens: 2 4 1 2.
At this point, we've reached a state we've seen before: 2 4 1 2 was
already seen. The infinite loop is detected after the fifth block
redistribution cycle, and so the answer in this example is 5.

Given the initial block counts in your puzzle input, how many
redistribution cycles must be completed before a configuration
is produced that has been seen before?
"""
KNOWN_STATES = {}

def max_bank(memorybanks):
    """Given the list of memory bank values, return a tuple containing:
       - the position of the maximum memory bank
       - the value at this position
    """
    maxval = max(memorybanks)
    maxidx = memorybanks.index(maxval)
    return (maxidx, maxval)

def cycle_banks(memorybanks, bank_idx):
    """Cycle banks to redistribute the memory pages in the bank_idx
       by starting the next memorybank"""
    start_sum = sum(memorybanks)
    redistribute = memorybanks[bank_idx]
    memorybanks[bank_idx] = 0
    while redistribute > 0:
        bank_idx = (bank_idx + 1) % len(memorybanks)        # next memory bank, consider wrap around
        memorybanks[bank_idx] += 1                          # add page to next
        redistribute -= 1                                   # decrease balance
    assert start_sum == sum(memorybanks)
    return memorybanks

def reset_known_states():
    """Reset the set of known states"""
    KNOWN_STATES.clear()

def known_state(memorybanks, statenumber=None):
    """Return if the current state is a known state; if not, add it
    to the known states and the statenumber!"""
    res = tuple(memorybanks) in KNOWN_STATES
    if not res:
        KNOWN_STATES[tuple(memorybanks)] = statenumber
    return res

def reallocate_memory(memorybanks):
    """Perform the reallocation until a known state occurs"""
    counter = 0
    while not known_state(memorybanks):
        idx, val = max_bank(memorybanks)
        memorybanks = cycle_banks(memorybanks, idx)
        counter += 1
        # print(f"Count: {counter} - banks: {memorybanks}")
    return counter

def statenumber(memorybanks):
    """Return the statenumber of the given configuration"""
    return KNOWN_STATES[tuple(memorybanks)]

def reallocate_memory_with_counter(memorybanks):
    """Perform the reallocation until a known state occurs"""
    counter = 0
    while not known_state(memorybanks, counter):
        idx, val = max_bank(memorybanks)
        memorybanks = cycle_banks(memorybanks, idx)
        counter += 1
        # print(f"Count: {counter} - banks: {memorybanks}")
    return counter - statenumber(memorybanks)

if __name__ == '__main__':
    banks = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]
    result = reallocate_memory_with_counter(banks)
    print(f"Reallaction encounters a known configuration after cycle {result}")
    # 6: 4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5 --> 12841
    # 6b 4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5 -->  8038
