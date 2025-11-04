""" 
A child class representing Circle

    Attributes:
    - x : read only (inherited)
    - y : read only (inherited)
    - radius (float) : read only 

    Computed properties:
    - area and perimeter are computed properties (read-only).
    - They are not stored as instance attributes because their values depend on the circle's radius.

    Methods:
    - translate(): to move x and y coordinates
    - inherited from parent class by default but not overriden.
    - is_unit_circle(): to return True if radius = 1, otherwise False

    Other info: 
    - compare shapes by their area and perimeter
    - Each child class implements its own formula for area and perimeter
    - Calculates area and perimeter using circle's own standard formulas
    - object info using __str__ and __repr__
""" 



from geometry import Geometry
from util import validate_positive_number
import math

class Circle(Geometry):
    def __init__(self, x = 0, y = 0, radius:float = 1):
        """
        - Validates that radius is a number imported from (validate_positive_number from util.py).
        - Inherit with super().__init__() to reuse code from Geometry.

        - In math geometry, plotting starts at 0
        - x and y are set to 0
        - x and y can be set by user later with incrementation +=

        - radius set to 1 as default, if not set in manual testing
        - no circle that radius = 0 exists or below, ValueError
        """
        super().__init__(x,y)
        validate_positive_number(radius)
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
        """User-friendly text output"""
        return (
        f"Circle with radius = {self._radius}\n"
        f"Coordinates = ({self.x}, {self.y})\n"
        f"Area = {round(self.area, 2)}\n"
        f"Perimeter = {round(self.perimeter, 2)}"
         )

    def __repr__(self):
        """Developer-friendly object output for debugging"""
        return (
        f"Circle(x={self.x}, y={self.y}, radius={self._radius},"
        f"area={round(self.area, 2)}, perimeter={round(self.perimeter, 2)})"
        )


