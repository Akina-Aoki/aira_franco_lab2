""" 
A child class representing Rectangle

    Attributes:
    - x : read only (inherited)
    - y : read only (inherited)
    - width (float): read only 
    - height (float): read only

    Computed properties:
    - area and perimeter are computed properties (read-only).
    - They are not stored as instance attributes because their values depend on the rectangle’s width and height.
    Don’t need to store W and H because they are computable.

    Methods:
    - translate(): to move x and y coordinates
    - inherited from parent class by default and overriden with additional logging.
    - Added console output
    - is_unit_square(): to return True if width == height, otherwise False

    Other info: 
    Stores the position (x, y) which has:
    - how shapes can move (translate method)
    - how to compare shapes by their area and perimeter
    - object info using __str__ and __repr__
    - Each child class implements its own formula for area and perimeter
    - Calculates area and perimeter using rectangle's own standard formulas
"""

from geometry import Geometry
from util import validate_positive_number
import math


class Rectangle(Geometry):
    """
    - In math geometry, plotting starts at 0
    - x and y are set to 0
    - x and y can be set by user later with incrementation +=
    - (x, y) = (width, height)
    - Inherits x and y from geometry property
    """
    def __init__(self, x:float = 0 , y:float = 0, width:float = 0, height:float = 0):
        
        """
        - Reuse validation imported form validate_number
        - Check x, y (already done in Geometry.py) are numbers in super().__init__
        - Width and height must be numbers (+ or -) OK for placement in any quadrant
        - Width and height cannot be equal values (this is not a square)
        - (x, y) = (0, 0) ORIGIN of the coordinate system
        - (width, height) stretches / plots it later to than width and height point (Vector)
        """
        super().__init__(x,y)

        # validate the width and height first before assigning below
        validate_positive_number(width)
        validate_positive_number(height)
    
        # assign instances last unique to rectangle
        self._width = width
        self._height = height

        
    # -------------------------
    #        PROPERTY
    # --------------------------
    """- x and y representing the center position of the object"""
    @property
    def width(self):
    # width rectangle read-only property
        return self._width

    @property
    def height(self):
    # height rectangle read-only property
        return self._height

    @property
    def area(self):
        # calculate rectangle area
        return self._width * self._height

    @property
    def perimeter(self):
    # calculate rectangle perimeter
        return 2 * (self._width + self._height)



    # --------------------------
    #         METHOD 
    # --------------------------
    """
    - Bug found here:
    I tried to print self.x_translate and self.y_translate, but those attributes don’t exist on the object.
    They’re just parameters to the translate() method, meaning they only exist as local variables, not as instance attributes.
        So inside the method,  reference them directly, not through self.
    """
    def translate(self, x_translate:float, y_translate:float):
        print(f"Move x coordinates by {x_translate}\ny coordinates by {y_translate}")
        super().translate(x_translate, y_translate)
        print(f"New rectangle coordinates:({self.x},{self.y})")


    """
    - Detecting a special case, not invalidating it
    - A square is not invalid, it is just a special case (square is a rectangle with 2 equal sides)
    """
    def is_unit_square(self) -> bool:
        """Return True if it is a square,  width == height."""
        if self.width == self.height:
            return True
        else:       
            return False
        



    # --------------------------
    #      REPRESENTATION
    # --------------------------
    
    def __str__(self):
        """User-friendly text output for print()"""
        return (
        f"Rectangle with width = {self._width}\n"
        f"Height = {self._height}\n"
        f"Area = {round(self.area, 2)}\n"
        f"Perimeter = {round(self.perimeter, 2)}"
        )

    def __repr__(self):
        """Developer-friendly object output for debugging"""
        return (
        f"Rectangle(x={self.x}, y={self.y}, "
        f"width={self._width}, height={self._height}, "
        f"area={round(self.area, 2)}, perimeter={round(self.perimeter, 2)})"
        )
