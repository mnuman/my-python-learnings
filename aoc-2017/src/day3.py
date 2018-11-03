"""You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and 
then counting up while spiraling outward. For example, the first few squares are 
allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
"""

def spiral(n):
    assert( n % 2)         # must be a truthy <> 0 value, i.e. n is odd!
    myarray = [[None]* n for j in range(n)]     # initialize a square n*n matrix
    x = n - 1
    y = n - 1
    dx, dy = -1, 0
    for i in range(n**2,0,-1):                  # bottom right is the start, has maximum value
        myarray[y][x] = i
        nx,ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n and myarray[ny][nx] == None:
            x,y = nx,ny
        else:
            dx,dy = -dy,dx
            x,y = x+dx, y+dy
    return myarray

def findvalue(array, val):
    for rowIdx, row in enumerate(array):
        if val in row:
            return (rowIdx, row.index(val))
    return (None, None)


def manhattan_distance(point1, point2):
    """ the distance on the grid is simply the sum of the difference in coordinates.
        since we donot know whether point1 or point2 is the larger one, we need to use
        the absolute values of the differences
    """
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

if __name__ == '__main__'    :
    array = spiral(561)
    p1 = findvalue(array, 1)
    p2 = findvalue(array, 312051)
    d = manhattan_distance(p1, p2)

    print(f"The distance between p1 and p2 is {d}")