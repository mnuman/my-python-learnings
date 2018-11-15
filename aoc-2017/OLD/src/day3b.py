"""
As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. 
Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, 
including diagonals.

So, the first few squares' values are chosen as follows:

Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ..."""

def getval(array,row,col):
    if array[row][col] == None:
        return 0
    else: 
        return array[row][col]


def calc_value(array, row, col):
    return max( (getval(array,row-1,col)+
                getval(array,row-1,col+1)+
                getval(array,row-1,col-1)+
                getval(array,row,col-1)+
                getval(array,row,col+1)+
                getval(array,row+1,col)+
                getval(array,row+1,col+1)+
                getval(array,row+1,col-1))
              , 1
    )


def adjacent_sum(n, threshold):
    assert( n % 2)                              # must be a truthy <> 0 value, i.e. n is odd!
    myarray = [[None]* n for j in range(n)]     # initialize a square n*n matrix
    row, col = n // 2, n // 2                   # start off in the center of the square now
    value = 0                                   # start value
    dr, dc = 0,1                                # initially moving in same row to nex column
    while value <= threshold:
        value = calc_value(myarray, row, col)
        myarray[row][col] = value
        row = row + dr
        col = col + dc
        # rotate counter clockwise as soon as we find a empty slot
        if myarray[row-dc][col+dr] == None:
            dr, dc = -dc, dr
    return value

if __name__ == '__main__'    :
    print(adjacent_sum(1001, 312051))
    # 312453