import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))

import day2
import unittest

class Day2Test(unittest.TestCase):
    def testReadlines(self):
        expected = [5, 1, 9, 5]
        r = day2.readfile(os.path.join(os.path.dirname(__file__), 'day2-test.txt'))
        self.assertListEqual(r[0], expected)

    def testCheckSum(self):
        r = day2.readfile(os.path.join(os.path.dirname(__file__), 'day2-test.txt'))
        self.assertEqual(day2.calc_checksum(r),18)