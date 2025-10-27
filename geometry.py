"""
geometry_lab/
├── geometry.py         # Geometry parent class
├── circle.py           # Circle shape
├── rectangle.py        # Rectangle shape
├── plotter.py          # Bonus: for drawing shapes
├── util.py             # Validation helpers
├── test_circle.py      # Unit tests
├── test_rectangle.py   # Unit tests
└── explorer.ipynb      # Manual test notebook

Inheritance → Rectangle and Circle will share a parent class (Geometry).

Polymorphism → Each shape has the same method names (area, perimeter) but works differently.

Composition → A separate class that has shapes inside it (not inherits from them).

Validation → Reuse the simple number validation from util.py.

"""
import math
from numbers import Number
from util import validate_number

class Geometry:
    """ 
    parent class for all geometric shapes.
    Stores the position (x, y) which has:
    - how shapes can move (translate)
    - how to compare shapes by their area
    - how to print object info using __str__ and __repr__

    """

    def __init__(self, x:float, y:float):
        """
        Create Geometry objects with x and y attributeas
        Validate that value is a number using is instance and one line for loop
        """
        if not all (isinstance(value, Number) for value in (x,y)):
            raise TypeError("x and y must be a number")
        self._x = x
        self._y = y

# -------------------------
#        PROPERTIES
# -------------------------

    # read only x property
    @property
    def x(self):
        return self._x
    
    # read only y property
    @property
    def y(self):
        return self._y


# ---------------------------------
#            METHODS
#----------------------------------
    """
    an operator overloads of comparison operator
    to check the value comparisons between values.

    AREA
    Geometry class contains the area comparison 
    since areas are comparable regardless of shape
    """

    def translate(self, x_translate:float, y_translate:float):
        """
        method to move x and y coordinates
        depending on the value,
        it is incremented x += x_translate and y += y_translate,
        store those new coordinates in (x_translate, y_translate)
        but not overwrties property _x and _y
        """
        if not all (isinstance(value, Number) for value in (x_translate, y_translate)):
            raise TypeError("x_translate and y_translate must BOTH be a number, NO STRINGS ALLOWED")
        self._x_translate = x_translate
        self._y = y_translate

# ---------------------------------
#         OPERATOR OVERLOAD
#----------------------------------
    """
    Comparison Operators (==, <, <=, >, >=)

    Comparison is based on the shape's area.
    The area is defined separately in each child class
    """

    def __eq__(self, value):
        if not isinstance(value, Geometry):
            return NotImplemented
        # used fot taking area for circle and rectangle
        return self.area == value.area
    
    def __lt__(self, value):
        return self.area < value.area
    
    def __le__(self, value):
        return self.area <= value.area
    
    def __gt__(self,value):
        return self.area > value.area
    
    def __ge__(self,value):
        return self.area >= value.area 
    

    # --------------------------
    #      REPRESENTATION
    # --------------------------
    
    def __str__(self):
        """
        user-friendly string display
        """
        return f"Geometry(parent class)\n(x = {self.x}, y = {self.y})"
    
    def __repr__(self):
        """
        developer string display (for debugging)
        """
        return f"Geometry(parent class)\n(x = {self.x}, y = {self.y})"