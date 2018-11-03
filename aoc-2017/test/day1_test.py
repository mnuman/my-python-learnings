import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))

import unittest
import day1

"""
1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
1111 produces 4 because each digit (all 1) matches the next.
1234 produces 0 because no digit matches the next.
91212129 produces 9 because the only digit that matches the next one is the last digit, 9.
"""
class Day1Test(unittest.TestCase):

    def test_1122(self):
        self.assertEqual(day1.day1('1122'), 3)

    def test_1111(self):
        self.assertEqual(day1.day1('1111'), 4)

    def test_1234(self):
        self.assertEqual(day1.day1('1234'), 0)

    def test_1212(self):
        self.assertEqual(day1.day1b('1212'), 6)

    def test_1221(self):
        self.assertEqual(day1.day1b('1221'), 0)

    def test_123425(self):
        self.assertEqual(day1.day1b('123425'), 4)

    def test_123123(self):
        self.assertEqual(day1.day1b('123123'), 12)

    def test_12131415(self):
        self.assertEqual(day1.day1b('12131415'), 4)

if __name__ == '__main__':
    unittest.main()
