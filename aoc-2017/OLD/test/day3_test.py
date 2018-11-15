import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))

import day3
import unittest

class Day3Test(unittest.TestCase):
    def test_spiral(self):
        array = day3.spiral(3)
        self.assertTrue(len(array) == 3)
        self.assertListEqual(array[0], [5,4,3])
        self.assertListEqual(array[1], [6,1,2])
        self.assertListEqual(array[2], [7,8,9])

    def test_coordinates(self):
        array = day3.spiral(3)
        row,col = day3.findvalue(array,1)
        self.assertTrue( row == 1 and col == 1 )
        row,col = day3.findvalue(array,7)
        self.assertTrue( row == 2 and col == 0 )

    def test_distances(self):
        array = day3.spiral(35)
        p1 = day3.findvalue(array,1)
        p12 = day3.findvalue(array,12)
        p23 = day3.findvalue(array,23)
        p1024 = day3.findvalue(array,1024)
        self.assertTrue(day3.manhattan_distance(p1,p1)  == 0)
        self.assertTrue(day3.manhattan_distance(p1,p12) == 3)
        self.assertTrue(day3.manhattan_distance(p12,p1) == 3)
        self.assertTrue(day3.manhattan_distance(p1,p23) == 2)
        self.assertTrue(day3.manhattan_distance(p1,p1024) == 31)

