
"""Unit testing module"""
# pylint: disable=C0111,E0401,C0304,C0413
import sys
import os
import random
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'src'))
import day11

def test_move_north():
  p = (0,0)
  assert day11.move(p, "n") == (0,-1)

def test_move_north_south():
  p = (8,3)
  assert day11.move(day11.move(p, "n"),"s") == p

def test_hex_distance_north():
  p = (0,0)
  assert day11.hex_distance(day11.move(p, "n"), p) == 1

def test_hex_distance_north_order():
  p = (0,0)
  assert day11.hex_distance(p, day11.move(p, "n")) == 1

def test_hex_distance_double_north():
  p = (0,4)
  assert day11.hex_distance(day11.move(day11.move(p, "n"), "n"), p) == 2

def testcase_distance_1():
  p = ( random.randint(-100,100), random.randint(-100,100))
  orig = p
  for mv in "ne,ne,ne".split(","):
    p = day11.move(p, mv)
  assert day11.hex_distance(orig,p) == 3

def testcase_distance_2():
  p = ( random.randint(-100,100), random.randint(-100,100))
  orig = p
  for mv in "ne,ne,sw,sw".split(","):
    p = day11.move(p, mv)
  assert day11.hex_distance(orig,p) == 0

def testcase_distance_3():
  p = ( random.randint(-100,100), random.randint(-100,100))
  orig = p
  for mv in "ne,ne,s,s".split(","):
    p = day11.move(p, mv)
  assert day11.hex_distance(orig,p) == 2

def testcase_distance_4():
  p = ( random.randint(-100,100), random.randint(-100,100))
  orig = p
  for mv in "se,sw,se,sw,sw".split(","):
    p = day11.move(p, mv)
  assert day11.hex_distance(orig,p) == 3

# ne,ne,sw,sw is 0 steps away (back where you started).
# ne,ne,s,s is 2 steps away (se,se).
# se,sw,se,sw,sw is 3 steps away (s,s,sw).