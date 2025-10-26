"""
Reuse util.py for validation (positive numbers)

"""

from numbers import Number

def validate_number(value:int):
    """
    Validate that the given value is a number.
    Value : any type
    Raises: TypeError if the value is not a number (int).
    Negative numbers are ok since x and y quadrants contains it.
    """
    if not isinstance(value, Number):   
        # checks if the value is a number
        raise TypeError(f"value must be a number, not {type(value)}")
    



    