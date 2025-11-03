"""
A child class representing Cube

Attributes:
- x : read-only (inherited from Geometry)
- y : read-only (inherited from Geometry)
- cube_side (float): read-only, represents the cube's edge length

Computed properties and formulas:
- cube_area (float): total surface area of the cube (6 × side²)
- cube_perimeter (float): total edge length (12 × side)
- cube_volume (float): space occupied (side³)

Methods:
- translate(): move cube’s (x, y) coordinates, inherited from Geometry
- comparison operators (==, <, >, etc.)

- __str__(): user-friendly text output
- __repr__(): developer-friendly object representation

Other info:
- In 3D shapes, a cube is bigger when it has a larger volume, not a larger surface (area).
- Compare cubes by volume first, and use area only if their volumes are the same.
- Implements its own formulas for cube_area, cube_perimeter and cube_volume.

Unit Testing: 
- Testng using pytest just to understand TDD
- Criterias to test is in the README
- pytest.approx() for floating-point results to avoid rounding issues
"""

from geometry import Geometry
from util import validate_positive_number  # same helper as util.py


class Cube(Geometry):
    def __init__(self, x: float = 0, y: float = 0, cube_side: float = 1):
        """
        Initialize a Cube object with position (x, y) and cube_side.
        Validates that cube_side is a positive number using validate_positive().
        """
        super().__init__(x, y)
        validate_positive_number(cube_side)
        self._cube_side = cube_side

    # -------------------------
    #        PROPERTY
    # -------------------------
    @property
    def cube_side(self):
        """Read-only edge length of the cube"""
        return self._cube_side

    @property
    def cube_area(self):
        """Total surface area = 6 × side²"""
        return 6 * (self._cube_side ** 2)

    @property
    def cube_perimeter(self):
        """Total edge length = 12 × side"""
        return 12 * self._cube_side

    @property
    def cube_volume(self):
        """Space occupied = side³"""
        return self._cube_side ** 3

    # --------------------------
    #         METHOD
    # --------------------------
    def translate(self, x_translate, y_translate):
        print(f"Move the coordinates by (x += {x_translate}, y += {y_translate})")
        super().translate(x_translate, y_translate)
        print(f"New coordinates: ({self.x}, {self.y})")

    # --------------------------
    #   OPERATOR OVERLOADING
    # --------------------------
    """
    Compare cubes by their size:
    - "==" returns True if both cubes have the same volume and area.
    - "<" compares cubes by volume first, and area if volumes are equal.
    """
    def __eq__(self, other):
        if not isinstance(other, Cube):
            return NotImplemented
        # both x and y volume and area must be the same
        return self.cube_volume == other.cube_volume and self.cube_area == other.cube_area
    

    def __gt__(self, other):
        # Check that the compared object is a Cube
        if not isinstance(other, Cube):
            return NotImplemented

         # When cube volumes are equal,
        # compare surface areas instead
        if self.cube_volume == other.cube_volume:
            return self.cube_area > other.cube_area

        # When volumes differ,
        # the cube with the larger volume is considered greater
        return self.cube_volume > other.cube_volume
    
    def __lt__(self, other):
        """Compare cubes by volume first, then by area if volumes are equal."""
        if not isinstance(other, Cube):
            return NotImplemented

        if self.cube_volume == other.cube_volume:
            return self.cube_area < other.cube_area
        return self.cube_volume < other.cube_volume

    


    # --------------------------
    #      REPRESENTATION
    # --------------------------
    def __str__(self):
        """User-friendly output"""
        return (f"Hello! I'm a cube with side {self._cube_side}.\n"
                f"My area is {self.cube_area}.\n"
                f"My perimeter is {self.cube_perimeter}.\n"
                f"My volume is {self.cube_volume}.")

    def __repr__(self):
        """Developer-friendly representation"""
        return f"Cube(cube_side={self._cube_side}, x={self.x}, y={self.y})"
