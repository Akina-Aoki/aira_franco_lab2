""" 
- Circle-specific pyscript, inherits Geometry
- This class adds a radius attribute
- Calculates area and perimeter using circle formulas
- Can check if it's a unit circle (radius = 1)
- Supports comparison operators for area (inherited from Geometry)
"""

from geometry import Geometry
from util import validate_number
import math

class Circle(Geometry):
    """
    Implements radius, area, and perimeter.
    """
    def __init__(self, x = 0, y = 0, radius:float = 1):
        """
        - Validates that radius is a number imported from (validate_number from util.py).
        - Uses super().__init__() to reuse code from Geometry.

        - In math geometry, plotting starts at 0
        - x and y are set to 0
        - x and y can be set by user later with incrementation +=

        - radius set to 1 as default
        - no circle that radius = 0 exists
        """
        super().__init__(x,y)

        # almost the same as validate_number, different approach
        if not isinstance(radius, (int, float)):
            # negative is ok, but not strings
            raise TypeError(f"Radius must be a number, not a {type(radius)}.")
        
        # assign attributes
        self._radius = radius
        
    # -------------------------
    #        PROPERTY
    # -------------------------
    @property
    def radius(self):
        """ radius read-only, cannot change radius"""
        return self._radius
    
    @property
    def area(self):
        """calcualtes area, formula:  π * r^2 """
        return math.pi * self._radius ** 2
    
    @property
    def perimeter(self):
        """calcualtes perimeter (circumference), formula: 2 * π * r"""
        return 2 * math.pi * self._radius


    # --------------------------
    #         METHOD
    # --------------------------
    def is_unit_circle(self):
        """
        - Checks if the circle is a unit circle
        - If unit is circle = True
        - Equation of a unit circle: x² + y² = 1
        - means x = 0, y = 0, radius = 1
        """
        print(f"x={self.x}, y={self.y}, radius={self.radius}")
        return self._radius == 1 and self.x == 0 and self.y == 0

    
    # --------------------------
    #      REPRESENTATION
    # --------------------------
    
    def __str__(self):
        return f"Hi! I am a circle class with a radius of {self._radius}\nand my coordinates are ({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Circle\nradius = {self._radius}, x={self.x}, y={self.y})"
    


