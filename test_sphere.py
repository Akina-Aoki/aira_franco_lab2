"""
run in terminal: pytest test_cube.py::"name of the method here" -v
to re run all: pytest test_cube.py -vv --cache-clear
re run but with one test:  pytest test_cube.py::"name of the method here" -vv --cache-clear
"""
import math
import pytest
from sphere import Sphere

"""
No arguments constructor
Ensures the default is (0, 0, 0) radius = 1
"""
def test_sphere_default():
    s1 = Sphere()
    assert s1.x == 0
    assert s1.y == 0
    assert s1.z == 0
    assert s1.radius # keep encapsulation clean. only touch public property


"""
Validates given inputs
Confirms that (x, y, z) radius == 5 are correcrt with asserted values
"""
def test_sphere_custom():
    s2 = Sphere(1, 1, 2, 5) # make sure it's an object, not tuple
    assert s2.x == 1
    assert s2.y == 1
    assert s2.z == 2
    assert s2.radius == 5

"""
Test for the string TypeError
"""
def test_sphere_invalid_string():
    with pytest.raises(TypeError) as error:
        Sphere(0, 0, 1, "string")
        print(error.value) # show type error message

"""Test for the negative ValueError"""
def test_sphere_invalid_negative():
    with pytest.raises(ValueError) as error:
        Sphere(2, 2, 2, -4)
        print(error.value)



"""Test for the 0 ValueError"""
def test_side_cube_invalid_zero():
    with pytest.raises(ValueError) as error:
        Sphere(2, 2, 2, 0)
        print(error.value)


# ----------------------------
#      Test Properties
# ----------------------------
    """Returns the sphere calculated properties by using the expected formula with math module
       and approx helps ignore tiny floating-point differences."""
    
def test_sphere_area():
    s3 = Sphere(2, 2, 2, 2)
    expected = 4 * math.pi * (2 ** 2)   # define expected before using it
    assert s3.sphere_area == pytest.approx(expected)

def test_sphere_volume():
    s3 = Sphere(2, 2, 2, 2)
    expected = (4/3) * math.pi * (s3.radius ** 3)
    assert s3.sphere_volume == pytest.approx(expected)
