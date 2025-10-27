""" 
- Rectangle-specific pyscript, inherits Geometry
- Inputs width and height for size
- Each child class implements its own formula for area and perimeter
- Calculates area and perimeter using rectangle's own standard formulas
"""

from geometry import Geometry
from util import validate_number
import math


class Rectangle(Geometry):
    """
    - In math geometry, plotting starts at 0
    - x and y are set to 0
    - x and y can be set by user later with incrementation +=
    - (x, y) = (width, height)
    - Inherits x and y from geometry property
    - 3 and 5 taken from the lab 3 test code sample, but could be any number later
    """
    def __init__(self, x = 0, y = 0, width:float = 3, height:float = 5):
        
        """
        - Reuse validation imported form validate_number
        - Check x, y (already done in Geometry.py) are numbers in super().__init__
        - Width and height must be numbers (+ or -) OK for placement in any quadrant
        - Width and height cannot be equal values (this is not a square)
        """
        super().__init__(x,y)

        # validate the width and height first before assigning below
        validate_number(width)
        validate_number(height)

        if width == height:
            raise ValueError("Width and height cannot be equal. This is not a square")
    
        # assign instances last unique to rectangle
        self._width = width
        self._height = height

        
    # -------------------------
    #        PROPERTY
    # --------------------------
    """x(width) and y(height) representing the center position of the object"""
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
    def is_unit_square(self) -> bool:
        """Return True if it is a square,  width == height."""
        print(f"It's a square.\n{self.width} == {self.height}.")
        return self.width == self.height



    # --------------------------
    #      REPRESENTATION
    # --------------------------
    
    def __str__(self):
        """User-friendly display"""
        return f"Hej! I'm a rectangle with a width of {self._width}\nand a height of {self._height}\nMy area is {self.area}.\nMy perimeter is{self.perimeter}"

    def __repr__(self):
        """Developer-friendly display"""
        return f"Rectangle\nwidth = {self._width}\nheight = {self._height}\nx = {self._x}\ny = {self._y}"
    
