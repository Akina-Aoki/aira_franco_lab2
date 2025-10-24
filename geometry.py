"""
geometry_lab/
├── geometry.py         # Geometry parent class
├── circle.py           # Circle shape
├── rectangle.py        # Rectangle shape
├── plotter.py          # Bonus: for drawing shapes
├── util.py             # Validation helpers
├── test_circle.py      # Unit tests
├── test_rectangle.py   # Unit tests
└── explore_manual.ipynb  # Manual test notebook

"""
import math

class Geometry:
    """
    - Parent class for the lab 3. Contains x and y
    - geometry parent class
    - shared methods: position, translation
    - x and y attributes shared by all shapes but has unique values
    - __str__
    - __repr__

    """

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

# ---------------------------------
#            METHODS
#----------------------------------

    # translate to move x and y???
    def translate(self, dx:int, dy:int):
        if not all(isinstance (i(int))for i in [dx, dy]):
            raise TypeError("Translate values must be integers.")
        self.x += dx
        self.y += dy

    """
    an operator overload of == to check equality
    Geometry class contains the area comparison 
    since areas are comparable regardless of formula
    """
    def __eq__(self, value):
        if not isinstance(value, Geometry):
            return NotImplemented
        # used fot taking area for circle and rectangle
        return self.area == value.area
    
    def __str__(self):
        """
        an override of __str__()
        user-friendly string display
        """
        return f"Geometry(parent class)\n(x = {self.x}, y = {self.y}"
    
    def __repr__(self):
        """
        an override of 
        __repr__()
        """
        return str(self)