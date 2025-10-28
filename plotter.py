"""
- Visual representation using matplotlib?

- might add a class like ShapePlotter or ShapeCollection that contains (not inherits) multiple shapes. this demonstrates composition.

- x and y representing the center and origin position of the object
"""

"""
plotter.py
Visualization helper for Geometry Lab 3.
Logic by Vector.plot() method.
"""

import matplotlib.pyplot as plt
from rectangle import Rectangle


class Plotter:
    """Plot geometric shapes (Rectangle now, Circle later)."""