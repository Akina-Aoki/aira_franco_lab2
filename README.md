# aira_franco_lab3
## Demonstrations of:

### Encapsulation → using private attributes (_attribute and __attribute).

### Validation and error handling → checking types and values inside setters or constructors.

### Inheritance → several examples of parent and child classes.

### Polymorphism → overridden methods across child classes.

### Modularity → creating small files or sections with reusable functions or methods.

________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
## References
### repo 
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
- In javaScript but similar logic: 

### Operator Overloading 
- Writing a rational class fraction in Python 
https://profound.academy/python-mid/fraction-class-xxyi3ExuVKFf7o8QdEjL?utm_source=chatgpt.com

- Operator Overloading 
https://www.programiz.com/python-programming/operator-overloading?utm_source=chatgpt.com 

- Operator Overloading - Magic Methods 
https://www.youtube.com/watch?v=m2JIBytk7Hg

### Validation
- Used same logic from OLD COIN STASH for validation in a util.py  
https://github.com/Akina-Aoki/python_course/tree/main/14_oop_inheritance 

### Plotting
- https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html?utm_source=chatgpt.com
- https://www.statology.org/matplotlib-rectangle/?utm_source=chatgpt.com
- https://www.geeksforgeeks.org/python/matplotlib-patches-rectangle-in-python/ 


| Concept / File                                      | In the GitHub repo example                                             | In your **geometry_lab3** project                                                                                     |
| --------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Validation helper** (`util.py`)                   | Validation often done inside the class itself                          | `util.py` – defines `validate_number()` for reusable number checking, imported by all shape classes (modularity)      |
| **Parent class** (`geometry.py`)                    | Base classes like `Animal`, `Vehicle`, etc., showing shared attributes | `Geometry` – defines `x`, `y`, `translate()`, and comparison operators for all geometric shapes                       |
| **Child class 1** (`circle.py`)                     | Example subclasses overriding methods (e.g., `Dog.speak()`)            | `Circle` – inherits from `Geometry`; defines its own `area`, `perimeter`, and string representation                   |
| **Child class 2** (`rectangle.py`)                  | Another subclass with its own unique behavior                          | `Rectangle` – inherits from `Geometry`; implements its own `area`, `perimeter`, `translate()`, and `is_unit_square()` |
| **Composition class** (`plotter.py`)                | Demonstrates “has-a” relationships or object containers                | `Plotter` – holds multiple shape objects (`Circle`, `Rectangle`) and visualizes them together with `matplotlib`       |
| **Manual test notebook 1** (`test_circle.ipynb`)    | Simple script files creating and testing instances                     | Tests for `Circle` class: creating, moving, comparing, and validating expected outputs                                |
| **Manual test notebook 2** (`test_rectangle.ipynb`) | Similar instance tests for subclasses                                  | Tests for `Rectangle`: creation, area/perimeter checks, translation, and `is_unit_square()` logic                     |
| **README.md**                                       | Explanation of class purpose and example output                        | Summarizes project structure, OOP principles used (inheritance, polymorphism, composition), and how to run tests      |


![Geometry CLass UML](https://github.com/user-attachments/assets/aa32dbac-c840-4787-a908-f132769c68b2)



