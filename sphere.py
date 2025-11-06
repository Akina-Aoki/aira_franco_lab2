from geometry import Geometry
from util import validate_positive_number, validate_number
import math
from numbers import Number

"""
Child class for Sphere in 3D

Attributes:
- x, y: inherited from Geometry
- z (float): extra coordinate for 3D position
- radius (float): distance from the center to the surface. Controls how big.

Formulas for sphere:
- sphere_area = 4 × π × r²
- sphere_volume = (4/3) × π × r³

Methods:
- translate(): move sphere around (x, y, z)
- comparison (==, <, >): compare by volume first, then area
"""

class Sphere(Geometry):
    # Create Sphere object
    def __init__(self, x:float|int = 0, y:float|int = 0, z:float|int = 0, radius:Number = 1):
        # validate z
        validate_number(z)

        #inheritance from Geometry x, y, already validated
        super().__init__(x, y)

        # validate radius using modularization
        validate_positive_number(radius)

        # instantiate z and radius
        self._z = z
        self._radius = radius

# ----------------------------
#          PROPERTY
# ----------------------------

    @property
    def z(self) -> float|int:
        """Read-only"""
        return self._z
    
    @property
    def radius(self) -> float|int:
        """Read-only"""
        return self._radius
    
    @property
    def sphere_area(self) -> float|int:
        """read-only calculated values"""
        return 4 * math.pi * (self._radius ** 2)
    
    @property
    def sphere_volume(self) -> float|int:
        """read-only calculated values"""
        return (4/3) * math.pi * (self._radius ** 3)
    
# ----------------------------
#          METHODS
# ----------------------------

    def translate(self, x_translate, y_translate, z_translate):
        """Move the sphere in space with full validation for all coordinates."""
        validate_number(x_translate)
        validate_number(y_translate)
        validate_number(z_translate)

        print(f"Move sphere by (x += {x_translate}, y += {y_translate}, z += {z_translate})")

        super().translate(x_translate, y_translate)
        self._z += z_translate

        print(f"New coordinates: ({self.x}, {self.y}, {self.z})")


# ----------------------------------
#       COMPARISON OPERATORS
# ---------------------------------

    def __eq__(self, other):
        """check 'other' is a Sphere object.
        If not, return NotImplemented to keep running """
        if not isinstance (other, Sphere):
            return NotImplemented
        return self.sphere_volume == other.sphere_volume
    
    def __lt__(self, other):
        """
        Compare two spheres.
        - Compare by volume first.
        - If volumes are equal, compare by surface area.
        """
        if not isinstance(other, Sphere):
            return NotImplemented
        if self.sphere_volume == other.sphere_volume:
            return self.sphere_area < other.sphere_area
        return self.sphere_volume < other.sphere_volume
    
    def __gt__(self, other):
        if not isinstance(other, Sphere):
            return NotImplemented
        if self.sphere_volume == other.sphere_volume:
            return self.sphere_area > other.sphere_area
        return self.sphere_volume > other.sphere_volume

    def __le__(self, other):
        """
        Just uses the logic already defined in __eq__, __lt__, and __gt__
        """
        if not isinstance(other, Sphere):
            return NotImplemented
        return self == other or self < other
    
    def __ge__(self, other):
        if not isinstance(other, Sphere):
            return NotImplemented
        return self == other or self > other

# -------------------------------
#          REPRESENTATION
# -------------------------------

    def __str__(self)->str:
        """User-friendly text output"""
        return (f"Hello! I'm a sphere\n"
            f"x = {self.x}, y = {self.y}, z = {self.z}\n"
            f"Sphere radius = {round(self._radius, 2)}\n"
            f"Volume = {round(self.sphere_volume, 2)}\n"
            f"Area = {round(self.sphere_area, 2)}"
        )

    def __repr__(self)->str:
        """Developer-friendly object output for debugging"""
        return (f"Sphere(x = {self.x}, y = {self.y}, z = {self.z}, radius = {self._radius})\n"
                f"Area = {(self.sphere_area, 2)}\n"
                f"Volume = {(self.sphere_volume, 2)}\n"
        )

