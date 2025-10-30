# aira_franco_lab2_ task1
## Demonstrations of:

- Encapsulation → using private attributes (_attribute and __attribute).

- Validation and error handling → checking types and values inside setters or constructors.

- Inheritance → several examples of parent and child classes.

- Polymorphism → overridden methods across child classes.

- Modularity → creating small files or sections with reusable functions or methods.


geometry_lab3/
├── geometry.py         # Geometry parent class
├── circle.py           # Circle child class
├── rectangle.py        # Rectangle child class
├── plotter.py          # plotting
├── util.py             # Validation helper
├── test_circle.py      # Unit tests
├── test_rectangle.py   # Unit tests

___________________________________________________________________________________________________________________________________________________



| Concept / File                                      | In the GitHub repo example                                             | In your **geometry_lab2** project                                                                                     |
| --------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Validation helper** (`util.py`)                   | Validation often done inside the class itself                          | `util.py` – defines `validate_number()` for reusable number checking, imported by all shape classes (modularity)      |
| **Parent class** (`geometry.py`)                    | Base classes like `Animal`, `Vehicle`, etc., showing shared attributes | `Geometry` – defines `x`, `y`, `translate()`, and comparison operators for all geometric shapes                       |
| **Child class 1** (`circle.py`)                     | Example subclasses overriding methods (e.g., `Dog.speak()`)            | `Circle` – inherits from `Geometry`; defines its own `area`, `perimeter`, and string representation                   |
| **Child class 2** (`rectangle.py`)                  | Another subclass with its own unique behavior                          | `Rectangle` – inherits from `Geometry`; implements its own `area`, `perimeter`, `translate()`, and `is_unit_square()` |
| **Composition class** (`plotter.py`)                | Demonstrates “has-a” relationships or object containers                | `Plotter` – holds multiple shape objects (`Circle`, `Rectangle`) and visualizes them together with `matplotlib`       |
| **Manual test notebook 1** (`test_circle.ipynb`)    | Simple script files creating and testing instances                     | Tests for `Circle` class: creating, moving, comparing, and validating expected outputs                                |
| **Manual test notebook 2** (`test_rectangle.ipynb`) | Similar instance tests for subclasses                                  | Tests for `Rectangle`: creation, area/perimeter checks, translation, and `is_unit_square()` logic                     |
| **README.md**                                       | Explanation of class purpose and example output                        | Summarizes project structure, OOP principles used (inheritance, polymorphism, composition), and how to run tests      |


![Blank diagram (1)](https://github.com/user-attachments/assets/4a6127fd-574c-465b-b7cf-40bd3cab7297)


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

### is_unit_square 
- LLM help: https://chatgpt.com/share/6901194b-5360-8003-8e80-4df1e7a423d2
  
### LLM Help with code
- https://chatgpt.com/g/g-p-68f8d0c6457c819183ed667899bce738-lab-3-geometry/shared/c/68fb3998-4f6c-8331-868f-f721178c1067?owner_user_id=user-NLscVkJ6P3VkgD6x67KkiwJE

### Plotting
#### Anatomy of a figure https://matplotlib.org/stable/gallery/showcase/anatomy.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html?utm_source=chatgpt.com
- https://www.statology.org/matplotlib-rectangle/?utm_source=chatgpt.com
- https://www.geeksforgeeks.org/python/matplotlib-patches-rectangle-in-python/
- Help with LLM: https://chatgpt.com/g/g-p-68f8d0c6457c819183ed667899bce738-lab-3-geometry/shared/c/6900cbdb-26d4-832b-8e84-6b5a39026b99?owner_user_id=user-NLscVkJ6P3VkgD6x67KkiwJE 

