"""
run in terminal: pytest test_cube.py::"name of the method here" -v
"""

import pytest
from cube import Cube

# Create test_cube (Should pass)
def test_cube_create():
    c1 = Cube(0, 0, 1)
    assert c1.x == 0
    assert c1.y == 0
    assert c1.cube_side == 2

# ------------------------
#     Test side_cube
# ------------------------

# Create test for the string
# Output:(Fail String TypeError)

def test_side_cube_invalid_string():
    with pytest.raises(TypeError) as error:
        Cube(1, 1, "string")
        print(error.value) # show type error message

# Create test for the negative
# Output:(Fail String ValueError)
def test_side_cube_invalid_negative():
    with pytest.raises(ValueError) as error:
        Cube(2, 2, -4)
        print(error.value)

# Create test for the 0
# Output:(Fail String ValueError)
def test_side_cube_invalid_zero():
    with pytest.raises(ValueError) as error:
        Cube(2, 2, 0)
        print(error.value)

# ----------------------------
#      Test Properties
# ----------------------------

def test_cube_area():
    c2 = Cube(2, 2, 2)
    assert c2.cube_area == pytest.approx(24)