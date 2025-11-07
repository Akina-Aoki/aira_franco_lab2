# aira_franco_lab2
# Video Link: https://stise-my.sharepoint.com/:v:/g/personal/aira_franco_stud_sti_se/EXht_Bw055NOn1rnmicQ0vkBfpYCSQiJEAuZWkqsNJdWfg?e=voYlRn

# Demonstrations of these OOP concepts:

- Encapsulation → using private attributes (_attribute and __attribute).

- Validation and error handling → checking types and values inside setters or constructors.

- Inheritance → several examples of parent and child classes.

- Polymorphism → overridden methods across child classes.

- Modularity → creating small files or sections with reusable functions or methods.

<br>
geometry_lab2/<br>
├── assets              # images UML<br>
├── util.py             # Validation helper<br>
├── geometry.py         # Geometry parent class<br>
<br>
Task 1:
<br>
├── circle.py           # Circle child class<br>
├── test_circle.py      # Unit tests<br>
├── test_circle.ipynb   # Manual tests<br>
├── rectangle.py        # Rectangle child class<br>
├── test_rectangle.py   # Unit tests<br>
├── test_rectangle.ipynb   # Manual tests<br>
├── plotter_task1.py    # plotting for circle and rectangle<br>
<br>
Task 2:
<br>
├── cube.py             # Cube child class<br>
├── test_cube.py        # Unit tests<br>
├── cube_check.ipynb    # double checking <br>
├── sphere.py           # Cube child class<br>
├── test_sphere.py      # Unit tests<br>

# UML
![alt text](<UML Lab 2.jpeg>)



___________________________________________________________________________________________________________________________________________________

# Task 1: Circle and Rectangle

```text
| Concept / File                         | In **geometry_lab2** project                                                |
| -------------------------------------- | --------------------------------------------------------------------------- |
| **Validation helper** (`util.py`)      | Checks numbers for reuse in all shapes                                      |
| **Parent class** (`geometry.py`)       | Base class with `x`, `y`, `translate()`, and comparison methods             |
| **Child class 1** (`circle.py`)        | Adds circle formulas for `area`, `perimeter`, and print info                |
| **Child class 2** (`rectangle.py`)     | Adds rectangle formulas and `is_unit_square()` check                        |
| **Composition** (`Shape2Dplotter.py`)  | Combines `Circle` and `Rectangle` to plot them with `matplotlib`            |
| **Manual test** (`test_circle.ipynb`)  | Tests `Circle` interactively: creation, move, compare, and errors           |
| **Manualtest** (`test_rectangle.ipynb`)| Tests `Rectangle`: area, move, and square check                             |
| **Unit test** (`test_circle.py`)       | Pytest for `Circle`: values, invalid input, and comparisons                 |
| **Unit test** (`test_rectangle.py`)    | Pytest for `Rectangle`: size, errors, move, and methods                     |
| **README.md**                          | Overview of classes, structure, and tests                                   |
```


#### In what context gets to decide on what is bigger? 
#### Circle and Rectangle: 
Area decides which shape is bigger.
Perimeter is only used as a tiebreaker when areas match.

| Concept       | What it measures                  | Units        |
| ------------- | --------------------------------- | ------------ |
| **Area**      | How much surface the shape covers | square units |
| **Perimeter** | The total boundary length         | linear units |
<br>


## Overview of Circle Class

| **Category**                         | **Feature / Case**       | **Example Input**                       | **Expected Behavior / Assertion**                            |
| ------------------------------------ | ------------------------ | --------------------------------------- | ------------------------------------------------------------ |
| **1️   Creation / Constructor**       | Default circle           | `Circle()`                              | x=0, y=0, radius=1                                           |
|                                      | Custom circle            | `Circle(2, 3, 5)`                       | x=2, y=3, radius=5                                           |
|                                      | Negative or zero radius  | `Circle(1, 1, 0)` or `Circle(1, 1, -3)` | `ValueError` (radius must be positive)                       |
|                                      | Non-numeric radius       | `Circle(1, 1, "abc")`                   | `TypeError`                                                  |
| **2️   Properties (Read-Only)**       | Radius is read-only      | `c = Circle(); c.radius = 5`            | Should raise `AttributeError`                                |
| **3️   Computed Properties**          | Area formula             | `Circle(0,0,2)`                         | `area == π * 2²` (≈12.566)                                   |
|                                      | Perimeter formula        | `Circle(0,0,2)`                         | `perimeter == 2 * π * 2` (≈12.566)                           |
| **4️   Validation of Coordinates**    | Negative x/y allowed     | `Circle(-1, -2, 3)`                     | Works normally (no error)                                    |
|                                      | Zero coordinates allowed | `Circle(0, 0, 3)`                       | Works normally                                               |
| **   Unit Circle Check**            | True if unit circle      | `Circle(0, 0, 1)`                       | `is_unit_circle()` → `True`                                  |
|                                      | False if not unit circle | `Circle(1, 0, 1)` or `Circle(0, 0, 2)`  | `is_unit_circle()` → `False`                                 |
| **6️   Comparison Operators**         | Equal circles            | Two circles with same radius            | `c1 == c2` → `True`                                          |
|                                      | Greater / smaller area   | radius 3 vs radius 2                    | `c1 > c2` → `True`; `c2 < c1` → `True`                       |
| **7️   Translate Method (Inherited)** | Move coordinates         | `c.translate(2, 3)`                     | x increases by 2, y increases by 3                           |
|                                      | Invalid input types      | `c.translate("a", 5)`                   | `TypeError`                                                  |
| **8️   String Representation**        | User-friendly print      | `print(c)`                              | Should display radius, area, perimeter nicely                |
|                                      | Developer print          | `repr(c)`                               | Returns clear dev format: `Circle(x=..., y=..., radius=...)` |


## Overview of Rectangle Class


## translate()

| Class         | Where `translate()` comes from | Behavior                                         | Prints extra info? |
| ------------- | ------------------------------ | ------------------------------------------------ | ------------------ |
| **Geometry**  | Original definition            | Base coordinate translation                      | No                 |
| **Circle**    | Inherited from Geometry        | Moves the center position                        | No                 |
| **Rectangle** | Overridden + calls `super()`   | Moves the shape and prints before/after movement | Yes                |


## Unit Testing for Circle and Rectangle

| **Class**                  | **What I want to test**                       |
| -------------------------- | --------------------------------------------- |
| **Creating a circle**      | Default, custom, zero, negative, wrong type   |
| **Properties**             | Area, perimeter, float values                 |
| **Translate (2D)**         | Moving coordinates, invalid input types       |
| **Comparing circles**      | Equal, larger, smaller comparisons            |
| -------------------------- | --------------------------------------------- |
| **Creating a rectangle**   | Default, custom, wrong types                  |
| **Properties**             | Area, perimeter, unit square check            |
| **Translate (2D)**         | Moving coordinates, invalid input types       |
| **Comparing rectangles**   | Equal, larger, smaller comparisons            |


________________________________________________________________________________________________________________________________________________
# Task 2: Cube and Sphere

| Attribute                | Cube                             | Sphere                           | Description                                             |
| ------------------------ | -------------------------------- | -------------------------------- | ------------------------------------------------------- |
| **x**                    | inherited from `Geometry`        | inherited from `Geometry`        | Horizontal position on the 3D plane                     |
| **y**                    | inherited from `Geometry`        | inherited from `Geometry`        | Vertical position on the 3D plane                       |
| **z**                    | defined in `Cube`                | defined in `Sphere`              | Depth coordinate showing position in 3D space           |
| **cube_side**            | unique to Cube                   | —                                | Length of one edge of the cube                          |
| **radius**               | —                                | unique to Sphere                 | Distance from the center to the surface                 |
| **cube_area**            | computed                         | —                                | Surface area of a cube = 6 × side²                      |
| **sphere_area**          | —                                | computed                         | Surface area of a sphere = 4 × π × r²                   |
| **cube_volume**          | computed                         | —                                | Volume of a cube = side³                                |
| **sphere_volume**        | —                                | computed                         | Volume of a sphere = (4/3) × π × r³                     |
| **cube_perimeter**       | computed                         | —                                | Total edge length of a cube = 12 × side                 |
| **translate()**          | inherited and extended (x, y, z) | inherited and extended (x, y, z) | Moves the shape’s position in 3D space                  |
| **comparison operators** | compares by volume, then area    | compares by volume, then area    | Defines how one shape is larger or smaller than another |


## Cube Unit Testing with pytest

| **Area**                | **What I want to test**        | **Example**                    | **What should happen**                                      |
| ----------------------- | ------------------------------ | ------------------------------ | ----------------------------------------------------------- |
| **Creating a cube**     | Try default values             | `Cube()`                       | Should create a cube at (0, 0, 0) with side = 1             |
|                         | Try custom values              | `Cube(2, 3, 4, 6)`             | Should set x = 2, y = 3, z = 4, cube_side = 6               |
|                         | Side = 0                       | `Cube(0, 0, 0, 0)`             | Should raise **ValueError** (side can’t be 0)               |
|                         | Side is negative               | `Cube(0, 0, 0, -4)`            | Should raise **ValueError** (side can’t be negative)        |
|                         | Side is not a number           | `Cube(0, 0, 0, "five")`        | Should raise **TypeError**                                  |
| ----------------------- | -----------------------------  | ------------------------------ | ----------------------------------------------------------- |
| **Properties**          | Check area formula             | side = 2 → 6 × 2²              | Should return **24**                                        |
|                         | Check perimeter formula        | side = 2 → 12 × 2              | Should return **24**                                        |
|                         | Check volume formula           | side = 3 → 3³                  | Should return **27**                                        |
|                         | Try a float value              | side = 2.5                     | Should work and return decimals (e.g. **15.625** volume)    |
| ----------------------- | -----------------------------  | ------------------------------ | ----------------------------------------------------------- |
| **Translate (3D)**      | Move all axes (x, y, z)        | `translate(2, 3, 4)`           | x = 2, y = 3, z = 4 (moved correctly in 3D space)           |
|                         | Move only x and y              | `translate(1, 1)`              | z should stay the same                                      |
|                         | Move only z                    | `translate(0, 0, 2)`           | Only z should increase by 2                                 |
|                         | Use wrong type                 | `translate("a", 5, 1)`         | Should raise **TypeError**                                  |
| ----------------------- | -----------------------------  | ------------------------------ | ----------------------------------------------------------- |
| **Comparing cubes**     | Equal cubes                    | same side = equal              | Should return **True**                                      |
|                         | Bigger vs smaller cube         | side 3 vs side 2               | Should return **True** for cube with larger volume          |
|                         | Same volume but different area | e.g. 3 vs 2.99 (slight diff)   | Should compare by **area as tiebreaker**                    |




## References
### repos reference 
- https://github.com/mirzayasirabdullahbaig07/OOP-In-Python.git
- https://github.com/GergesHany/object-oriented-programming-OOP-/tree/main/Polymorphism
- https://github.com/MostafaAhmed98/Python_OOP_Projects
- 
### Inheritance OOP 
- https://realpython.com/inheritance-composition-python/
- https://www.geeksforgeeks.org/python/polymorphism-in-python/

### Polymorphism
- https://www.youtube.com/watch?v=tHN8I_4FIt8
- lecture notes: 15_oop_polymorphism

### Geometry shapes and OOP
- https://www.youtube.com/watch?v=2nB1ktGbLB4
In javaScript but similar logic: 

### Operator Overloading 
- functools
https://docs.python.org/3/library/functools.html#functools.total_ordering 

- Writing a rational class fraction in Python<br>
https://profound.academy/python-mid/fraction-class-xxyi3ExuVKFf7o8QdEjL?utm_source=chatgpt.com

- Operator Overloading <br>
https://www.programiz.com/python-programming/operator-overloading?utm_source=chatgpt.com 

- Operator Overloading - Magic Methods <br>
https://www.youtube.com/watch?v=m2JIBytk7Hg

### Validation
- Used same logic from OLD COIN STASH for validation in a util.py  
https://github.com/Akina-Aoki/python_course/tree/main/14_oop_inheritance

### is_unit_square 
- LLM help: https://chatgpt.com/share/6901194b-5360-8003-8e80-4df1e7a423d2

### Cube area, perimeter and volume
- https://blog.finxter.com/5-best-ways-to-calculate-the-area-of-a-cube-using-python/

- https://blog.finxter.com/5-best-ways-to-calculate-the-volume-of-a-cube-in-python/

-  pytest.approx()
https://thewebdev.info/2024/04/07/how-to-assert-almost-equal-with-python-pytest/ 



### Plotting Circle and Rectangle 2D
- Anatomy of a figure 
https://matplotlib.org/stable/gallery/showcase/anatomy.html

- https://www.statology.org/matplotlib-rectangle/?utm_source=chatgpt.com

- https://www.geeksforgeeks.org/python/matplotlib-patches-rectangle-in-python/


- add_patch
https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch

- axes.text
https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text

- MplRectangle Matplotlib
https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html

- MplCircle
https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html

- plt.subplots()
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html

- hasattr(obj, name)
https://www.geeksforgeeks.org/python/python-hasattr-method/ 


- set_aspect
https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect

- ax.grid()
https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid

- ax.autoscale()
https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale.html#matplotlib.axes.Axes.autoscale
