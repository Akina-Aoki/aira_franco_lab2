import math
from numbers import Number
from util import validate_number, validate_positive_number


class Geometry:
    """ 
    A parent class representing Geometry

    Attributes:
    - x (float): read only
    - y (float): read only

    Methods:
    - translate(): method to move x and y coordinates
    
    Operator Overloading:

    Stores the position (x, y) which has:
    - how shapes can move (translate method)
    - how to compare shapes by their area and perimeter
    - object info using __str__ and __repr__
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
    """x and y representing the center / origin position of the object"""

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
        depending on the value, the new values are incremented to x += x_translate and y += y_translate.

        - Bug here when testing circle and rectangle: DECISION: Will not make a reset button. Just run once.
        - translate() method doesn’t “reset” the rectangle’s position, it increments to its current coordinates.
        """
        if not all (isinstance(value, Number) for value in (x_translate, y_translate)):
            raise TypeError("x_translate and y_translate must BOTH be a number, NO STRINGS ALLOWED")
        self._x += x_translate
        self._y += y_translate


# ---------------------------------
#         OPERATOR OVERLOAD
#----------------------------------
    """
    - Both Circle and Rectangle have their own area and perimeter implementations,
    it gives universal comparison logic that works for any shape class.

    - The result of the value of each circle's area and perimeter will be used for testing
    and operation overloading below.

    - If areas are equal, perimeter will be used as a TIEBRAKER.
    - self = x, value = y (that's just how it is)
    - Do not crashes and ignored with "NotImplemented" when a non-existent value is given.
    """

    def __eq__(self, value):
        if not isinstance(value, Geometry):
            return NotImplemented
        return (self.area, self.perimeter) == (value.area, value.perimeter)
    
    def __lt__(self, value):
        if not isinstance(value, Geometry):
            return NotImplemented
        return (self.area, self.perimeter) < (value.area, value.perimeter)
    
    def __le__(self, value):
        if not isinstance(value, Geometry):
            return NotImplemented
        return (self.area, self.perimeter) <= (value.area, value.perimeter)
    
    def __gt__(self,value):
        if not isinstance(value, Geometry):
            return NotImplemented
        return (self.area, self.perimeter) > (value.area, value.perimeter)
    
    def __ge__(self,value):
        if not isinstance(value, Geometry):
            return NotImplemented
        return (self.area, self.perimeter) >= (value.area, value.perimeter)
    

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