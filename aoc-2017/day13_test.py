"""Test module for functions of Advent of Code, day13"""
import os
import day13
# pylint: disable=C0111,C0303


def test_read_file_test():
    myfirewall = day13.read_configuration(os.path.join(
        os.path.dirname(__file__), 'day13_test.txt'))
    assert len(myfirewall.layers) == 7
    assert myfirewall.layers[0].depth == 3
    assert myfirewall.layers[1].depth == 2
    assert myfirewall.layers[2].depth is None
    assert myfirewall.layers[3].depth is None
    assert myfirewall.layers[4].depth == 4
    assert myfirewall.layers[5].depth is None
    assert myfirewall.layers[6].depth == 4
    # not yet started
    assert myfirewall.packet_position == -1
    assert myfirewall.packet_score == 0


def test_move():
    myfirewall = day13.read_configuration(os.path.join(
        os.path.dirname(__file__), 'day13_test.txt'))
    # all position on origin
    assert myfirewall.layers[0].pos == 0
    assert myfirewall.layers[1].pos == 0
    assert myfirewall.layers[2].pos is None
    assert myfirewall.layers[3].pos is None
    assert myfirewall.layers[4].pos == 0
    assert myfirewall.layers[5].pos is None
    assert myfirewall.layers[6].pos == 0
    myfirewall.move_scanners()
    # all positions have moved
    assert myfirewall.layers[0].pos == 1
    # this is the maximum depth, hence invert after this step !
    assert myfirewall.layers[1].pos == 1
    assert myfirewall.layers[2].pos is None
    assert myfirewall.layers[3].pos is None
    assert myfirewall.layers[4].pos == 1
    assert myfirewall.layers[5].pos is None
    assert myfirewall.layers[6].pos == 1
    myfirewall.move_scanners()
    # slot 0 must moved to maxdepth
    assert myfirewall.layers[0].pos == 2
    # slot 1 must have returned to origin
    assert myfirewall.layers[1].pos == 0
    myfirewall.move_scanners()
    # slot 0 has inverted and stepped back to pos 2 (=1)
    assert myfirewall.layers[0].pos == 1
    # slot 1 has moved forward again
    assert myfirewall.layers[1].pos == 1
    # three steps taken
    assert myfirewall.layers[4].pos == 3


def test_pass_through():
    myfirewall = day13.read_configuration(os.path.join(
        os.path.dirname(__file__), 'day13_test.txt'))

    while myfirewall.packet_position < len(myfirewall.layers):
        myfirewall.cycle()
    # caught at layer 0 - depth 3 and layer 6 - depth 4
    assert myfirewall.packet_score == 24


def test_pass_through_2():
    myfirewall = day13.read_configuration(os.path.join(
        os.path.dirname(__file__), 'day13_test2.txt'))
    while myfirewall.packet_position < len(myfirewall.layers):
        myfirewall.cycle()
    # caught at layer 0, 2, 4, 6, 8 all depth 2
    assert myfirewall.packet_score == (0 + 2 + 4 + 6 + 8) * 2


def test_pass_solve():
    myfirewall = day13.read_configuration(os.path.join(
        os.path.dirname(__file__), 'day13_test.txt'))

    delay = day13.solve(myfirewall)
    assert delay == 10
