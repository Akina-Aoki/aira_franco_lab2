""" 
Circle-specific logic, inherits Geometry
This script will calculate the radius of a circle from their x, y axis and 
use operator overloading to calculate the comparison of  values
between circle_1 and circle_2
"""

from geometry import Geometry

class Circle(Geometry):
    def __init__(self, radius:float):
        super().__init__(x,y)

        # create instances unique to circle
        self._radius = radius

        """
        Validation, check x, y and radius are integers
        """
        try:
            if not isinstance (x, int) or not (y, int) or not (radius, int):
                raise TypeError("All values must be integer s")
            # store all attributes as objects
            self.value = (x, y, radius)

        except TypeError as e:
            print(f"Error {e}")
            raise # stop program if invalid inputs are used


    # -------------------------
    #        PROPERTY
    # -------------------------
    @property

    # --------------------------
    #         METHOD
    # --------------------------
    def area(self):
        return math.pi * self.radius ** 2   