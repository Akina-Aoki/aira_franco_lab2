""" 
This script will calculate the radius of a circle from their x, y axis and 
use operator overloading to calculate the comparison of  values
between circle_1 and circle_2
"""

from rectangle import Rectangle

class Rectangle:
    def __init__(self, x:int, y:int, height:int, width:int):
        """
        Validation, check x, y and radius are integers
        """
        try:
            if not isinstance (x, int) or not (y, int) or not (radius, int):
                raise TypeError("All values must be integer s")
            # store all attributes as objects
            self.value = (x, y, height, width)

        except TypeError as e:
            print(f"Error {e}")
            raise # stop program if invalid inputs are used

        # create instances
        self._x = x
        self._y = y
        self._height = height
        self._width = width
    # -------------------------
    #        PROPERTY
    # --------------------------




# ---------------
#     METHODS
# ----------------

    def area(self):
    