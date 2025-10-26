""" 
- Rectangle-specific pyscript, inherits Geometry

- 

- Each child class implements its own formula for area and perimeter
"""

from geometry import Geometry
from util import validate_number
import math


class Rectangle(Geometry):
    def __init__(self, width:int, height:int):
        super().__init__(x,y)

        # create instances unique to rectangle
        self._width = width
        self._height = height
        """
        Validation, check x, y and radius are integers
        """
        try:
            if not isinstance (x, int) or not (y, int) or not (radius, int):
                raise TypeError("All values must be integer s")
            # store all attributes as objects
            self.value = (x, y, width, height)

        except TypeError as e:
            print(f"Error {e}")
            raise # stop program if invalid inputs are used

        
    # -------------------------
    #        PROPERTY
    # --------------------------
    @property


    # --------------------------
    #         METHOD
    # --------------------------
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2* (self.width * self.height)
    
    def __str__(self):
        return (self)

    def __repr__(self):
        return f"Rectangle\nwidth = {self._width}\nheight = {self._height}"
    
rectangle = Rectangle(x=0, y=0, width=1, height=1) 
rectangle2 = Rectangle(width=3, height="5") # raise TypeError