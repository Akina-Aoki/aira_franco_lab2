"""
geometry_lab3/
├── geometry.py         # Geometry parent class
├── circle.py           # Circle child class
├── rectangle.py        # Rectangle child class
├── plotter.py          # drawing shapes
├── util.py             # Validation helper
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
    """x and y representing the center position of the object"""

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

    def translate(self, x_translate:float, y_translate:float):
        """
        - method to move x and y coordinates
        depending on the value, it is incremented x += x_translate and y += y_translate

        - new coordinates in (x_translate, y_translate)
        increment to property _x and _y

        - Bug here when testing rectangle: DECISION PENDING
        - translate() method doesn’t “reset” the rectangle’s position, it adds to its current coordinates.
        - Just want to “set position” not "increment position" during tests
        """
        if not all (isinstance(value, Number) for value in (x_translate, y_translate)):
            raise TypeError("x_translate and y_translate must BOTH be a number, NO STRINGS ALLOWED")
        self._x += x_translate
        self._y += y_translate

   
   
    """ 
    def move_to(self, new_x: float, new_y: float):
    # Move shape to exact new coordinates (overwrite x and y).
    if not all(isinstance(value, Number) for value in (new_x, new_y)):
        raise TypeError("new_x and new_y must both be numbers")
    self._x = new_x
    self._y = new_y
    """


# ---------------------------------
#         OPERATOR OVERLOAD
#----------------------------------
    """
    - Comparison Operators (==, <, <=, >, >=)
    - Comparison is based on the shape's area.
    - The area is defined separately in each child class
    - The result of the value of each circle's area will be used for testing later
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
        return f"Hello! My name is Geometry. I'm the parent class. hohoho!\nMy coordinates are({self.x}, {self.y})"
    
    def __repr__(self):
        """
        developer string display (for debugging)
        """
        return f"Geometry(parent class)\n(x = {self.x}, y = {self.y})"