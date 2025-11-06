"""
run in terminal: pytest test_rectangle.py::"name of the method here" -v
to re run all: pytest test_rectangle.py -vv --cache-clear
re run but with one test:  pytest test_rectangle.py::"name of the method here" -vv --cache-clear
"""

import pytest
from rectangle import Rectangle
import math


"""
No arguments constructor
Ensures default is (0, 0, width=0, height=0)
Raises an error if the value is zero or negative
"""
def test_rectangle_default():
    r1 = Rectangle()
    assert r1.x == 0
    assert r1.y == 0
    assert r1.width == 0
    assert r1.height == 0


"""
Validates inputs (x, y, width, height)
"""
def test_rectangle_custom():
    r2 = Rectangle(2, 3, 4, 5)
    assert r2.x == 2
    assert r2.y == 3
    assert r2.width == 4
    assert r2.height == 5


"""
Test for invalid string TypeError
"""
def test_rectangle_invalid_string():
    with pytest.raises(TypeError):
        Rectangle(1, 1, "width", 5)


"""
Test for invalid negative ValueError
"""
def test_rectangle_invalid_negative():
    with pytest.raises(ValueError):
        Rectangle(1, 1, -2, 4)


"""
Test for invalid zero ValueError
"""
def test_rectangle_invalid_zero():
    with pytest.raises(ValueError):
        Rectangle(0, 0, 0, 3)


"""
Testing area and perimeter formulas
"""
def test_rectangle_area_perimeter():
    r3 = Rectangle(1, 1, 4, 5)
    expected_area = 4 * 5
    expected_perimeter = 2 * (4 + 5)
    assert r3.area == expected_area
    assert r3.perimeter == expected_perimeter


"""
Testing translate() method
Should move x and y correctly
"""
def test_rectangle_translate():
    r4 = Rectangle(0, 0, 2, 3)
    r4.translate(5, 5)
    assert r4.x == 5
    assert r4.y == 5


"""
Testing is_unit_square()
Should return True if width == height
"""
def test_rectangle_is_unit_square_true():
    r5 = Rectangle(0, 0, 3, 3)
    assert r5.is_unit_square() == True


"""
Testing is_unit_square()
Should return False if width != height
"""
def test_rectangle_is_unit_square_false():
    r6 = Rectangle(0, 0, 4, 2)
    assert r6.is_unit_square() == False


"""
Testing comparison operators
"""
def test_rectangle_comparison():
    r7_small = Rectangle(1, 1, 2, 2)
    r8_large = Rectangle(1, 1, 4, 5)
    assert r8_large > r7_small
    assert r7_small < r8_large
    assert not (r7_small > r8_large)
    assert not (r8_large < r7_small)


"""
Testing tiebreaker:
Rectangles with same area but different perimeters
"""
def test_rectangle_tiebreaker_pass():
    """Testing same area but different perimeter"""
    # both have area = 12, but different perimeter
    r9 = Rectangle(0, 0, 3, 4)
    r10 = Rectangle(0, 0, 6, 2)

    # areas equal (3*4 == 6*2 == 12)
    assert math.isclose(r9.area, r10.area)

    # perimeter difference triggers tiebreaker
    assert r9.perimeter != r10.perimeter

    # the one with smaller perimeter should be smaller
    assert r9 < r10
