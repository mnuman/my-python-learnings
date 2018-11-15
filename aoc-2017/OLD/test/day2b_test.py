import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))

import day2b
import unittest

class Day2bTest(unittest.TestCase):
    def testReadlines(self):
        expected = [5, 9, 2, 8]
        r = day2b.readfile(os.path.join(os.path.dirname(__file__), 'day2b-test.txt'))
        self.assertListEqual(r[0], expected)

    def testCheckSum(self):
        r = day2b.readfile(os.path.join(os.path.dirname(__file__), 'day2b-test.txt'))
        self.assertEqual(day2b.calc_checksum(r),9)