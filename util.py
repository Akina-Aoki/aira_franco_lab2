"""
- Reuse utils from lecture for validation/error handling (numbers)
- Negative numbers are not rejected because there are negative quadrants
- String types are rejected
"""

from numbers import Number

def validate_number(value:int|float):
    """
    Validate that the given value is a number.
    Value : any type
    Raises: TypeError if the value is a string type.
    """
    if not isinstance(value, Number):   
        # checks if the value is NOT a number
        raise TypeError(f"value must be a number, not {type(value)}")
    



    