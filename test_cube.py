"""
run in terminal: pytest test_cube.py::"name of the method here" -v
to re run: pytest test_cube.py -vv --cache-clear
"""

import pytest
from cube import Cube


# just a debug trigger, to check that folder is running in earlier test
def test_run():
    pass


"""
No arguments constructor
Ensures the default is (0, 0, 1)
"""
def test_cube_default():
    c1 = Cube()     # no args
    assert c1.x == 0
    assert c1.y == 0
    assert c1.cube_side == 1



"""
Validates given inputs
Confirms that (x, y, side) are correcrt with asserted values
"""
def test_cube_custom():
    c3 = Cube(3, 3, 5)
    assert c3.x == 3
    assert c3.y == 3
    assert c3.cube_side == 5

# ------------------------
#     Test side_cube
# ------------------------

"""
Test for the string TypeError
"""

def test_side_cube_invalid_string():
    with pytest.raises(TypeError) as error:
        Cube(1, 1, "string")
        print(error.value) # show type error message


"""Test for the negative ValueError"""
def test_side_cube_invalid_negative():
    with pytest.raises(ValueError) as error:
        Cube(2, 2, -4)
        print(error.value)



"""Test for the 0 ValueError"""
def test_side_cube_invalid_zero():
    with pytest.raises(ValueError) as error:
        Cube(2, 2, 0)
        print(error.value)


# ----------------------------
#      Test Properties
# ----------------------------

"""
Pytest that cube_area returns 6 x side²
pytest.approx() to compare floating-point numbers safely
"""
def test_cube_area_pass():
    c2 = Cube(2, 2, 2)
    assert c2.cube_area == pytest.approx(24) # floting nums near 24 are passed

def test_cube_area_fail():
    c2 = Cube(2, 2, 2)
    assert c2.cube_area == pytest.approx(22.5) 


"""
Pytest that cube_perimeter returns 12 × side
"""
def test_cube_perimeter_pass():
    c2 = Cube(2, 2, 2)
    assert c2.cube_perimeter == pytest.approx(24)  # call the method from geometry, use pytest

def test_cube_perimeter_fail():
    c2 = Cube(2, 2, 2)
    assert c2.cube_perimeter == pytest.approx(12)


"""
Pytest that cube_perimeter returns side³
"""
def test_cube_volume_pass():
    c2 = Cube(2, 2, 2)
    print(c2.cube_volume)
    assert c2.cube_volume == pytest.approx(8)


def test_cube_volume_fail():
    c2 = Cube(2, 2, 2)
    print(c2.cube_volume)
    assert c2.cube_volume == pytest.approx(21.2)


""" Pytest that cube_float return decimals"""
def test_cube_float():
    c4 = Cube(2, 2, 2.5)  # try volume
    assert c4.cube_volume == pytest.approx(15.625)  # 15.625



# -------------------------------
#       Test Translate()
# -------------------------------

"""Move x and y coordiantes, check the asserted values pass"""
def test_cube_translate_pass():
    c5 = Cube(5, 5, 5)  #(x, y, sides)
    # from the cube.py, use translate() here to move coordinates by x, y+= 1
    c5.translate(1, 1)   
    assert c5.x == 6  # 5 + 1
    assert c5.y == 6  
    print(f"New coordinates: ({c5.x},{c5.y})")

"""Failed translate(), TypeError because of str"""
def test_cube_translate_TypeError():
    c5 = Cube(5, 5, 5)
    with pytest.raises(TypeError):
        c5.translate("A", 1)


# --------------------------
#     Comparing Cubes
# --------------------------
def test_cube_equal():
    c_large =(4, 4, 4)
    c_small = (2, 2, 4)    # side == side
    assert c_large == c_small  # True



