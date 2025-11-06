"""
run in terminal: pytest test_circle.py::"name of the method here" -v
to re run all: pytest test_circle.py -vv --cache-clear
re run but with one test:  pytest test_circle.py::"name of the method here" -vv --cache-clear
"""

import math
import pytest
from circle import Circle

"""cl
No arguments constructor
Ensures the default is (0, 0, 1) 
"""
def test_circle_default():
    c1 = Circle()  # no args
    assert c1.x == 0
    assert c1.y == 0
    assert c1.radius == 1

"""
Validates given inputs
Confirms that (x, y) radius are correcrt with asserted values
"""
def test_circle_custom():
    c2 = Circle(1, 2, 3)
    assert c2.x == 1
    assert c2.y == 2
    assert c2.radius == 3

"""
Test for the string TypeError
"""
def test_circle_invalid_string():
    with pytest.raises(TypeError):
        Circle(1, 1, "radius")

"""Test for the negative ValueError"""
def test_circle_invalid_negative():
    with pytest.raises(ValueError):
        Circle(0, 0, -4)

"""Test for the 0 ValueError"""
def test_side_circle_invalid_zero():
    with pytest.raises(ValueError):
        Circle(2, 2, 0)


# ----------------------------
#      Test Properties
# ----------------------------

"""
- Returns the circle's calculated properties by using the expected formula with math module
- Approx helps ignore tiny floating-point differences
- Check the actual results in the test_circle.ipynb"""

def test_circle_area():
    c3 = Circle(2, 2, 4)
    expected = math.pi * (c3.radius ** 2)    # define expected before using it
    assert c3.area == pytest.approx(expected)

def test_circle_perimeter():
    c3 = Circle(2, 2, 4)
    expected = 2 * math.pi * c3.radius
    assert c3.perimeter == pytest.approx(expected)


# -------------------------
#  COMPARISON OPERATORS
# -------------------------

def test_circle_equal_pass():
    """Test Circle Equality"""
    c1 = Circle(1, 1, 2)
    c2 = Circle(1, 1, 2)
    assert c1 == c2  # True

def test_circle_equal_fail():
    c1 = Circle(1, 1, 2)
    c2 = Circle(1, 1, 2)
    assert c1 != c2  # False

def test_circle_lt_pass():
    """Testing less than """
    c3 = Circle(2, 2, 4)
    c4 = Circle(3, 3, 5)
    assert c3 < c4  # True

def test_circle_gt_fail():
    """Testing greater than """
    c4 = Circle(3, 3, 5)
    c1 = Circle(1, 1, 2)
    assert c1 > c4  # False

def test_circle_tiebraker_pass():
    """Testing same area but different perimeter"""
    c5 = Circle(2, 2, 4)
    c6 = Circle(1, 1, 3)
    assert c5 > c6  # True → larger radius = larger area and perimeter

def test_circle_tiebraker_fail():
    c7 = Circle(2, 2, 4)
    c8 = Circle(1, 1, 4) 
    assert c7 > c8 # True


# -------------------------
#       TEST TRANSLATE
# -------------------------
"""Move x and y coordiantes, check the asserted values pass"""
def test_circle_translate(): # pass
    c5 = Circle(2, 2)
    c5.translate(1, 1)
    assert c5.x == 3
    assert c5.y == 3

def test_circle_translate_TypeError():
    """Failed translate(), TypeError because of str"""
    c6 = Circle(1, 1)
    with pytest.raises(TypeError):
        c6.translate(1, "one")

def test_positional_argument():
    """takes 3 positional arguments but 4 were given"""
    c6 = Circle(1, 1)
    c6.translate(1, 1, 2)

