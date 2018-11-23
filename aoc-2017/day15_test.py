import day15
import day15_generator


def test_binary_0():
    assert day15.toBinary(0) == '0'


def test_binary_1():
    assert day15.toBinary(1) == '1'


def test_another_number():
    assert day15.toBinary(432598043) == "11001110010001110110000011011"


def test_generator_A():
    gA = day15_generator.Generator(65, 16807)
    assert gA.generate() == 1092455
    assert gA.generate() == 1181022009
    assert gA.generate() == 245556042
    assert gA.generate() == 1744312007
    assert gA.generate() == 1352636452

    assert gA.generate() != 1352636452


def test_generator_B():
    gB = day15_generator.Generator(8921, 48271)
    assert gB.generate() == 430625591
    assert gB.generate() == 1233683848
    assert gB.generate() == 1431495498
    assert gB.generate() == 137874439
    assert gB.generate() == 285222916


def test_binary_lowbits():
    assert day15.binaryEqualLowBits(432598043, 432598043, 16)
    assert day15.binaryEqualLowBits(245556042, 1431495498, 16)
    assert not(day15.binaryEqualLowBits(245556042, 1431495498, 27))
    assert not(day15.binaryEqualLowBits(1744312007, 430625591, 16))


def test_generatorCompare_short():
    assert day15.generatorCompare(65, 16807, 8921, 48271, 5) == 1


# def test_generatorCompare_long():
#     assert day15.generatorCompare(65, 16807, 8921, 48271, 40000000) == 588


def test_generatorA_15B():
    gA = day15_generator.GeneratorB(65, 16807, 4)
    assert gA.generate() == 1352636452
    assert gA.generate() == 1992081072
    assert gA.generate() == 530830436
    assert gA.generate() == 1980017072
    assert gA.generate() == 740335192


def test_generatorB_15B():
    gB = day15_generator.GeneratorB(8921, 48271, 8)
    assert gB.generate() == 1233683848
    assert gB.generate() == 862516352
    assert gB.generate() == 1159784568
    assert gB.generate() == 1616057672
    assert gB.generate() == 412269392


def test_generatorCompareB():
    gA = day15_generator.GeneratorB(65, 16807, 4)
    gB = day15_generator.GeneratorB(8921, 48271, 8)
