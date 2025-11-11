"""
- Reuse utils from lecture for validation/error handling (numbers)
- Negative numbers and 0 are rejected
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
    
    
def validate_positive_number(value:int|float):
    if not isinstance(value,Number):
        raise TypeError(f"value must be a number, not {type(value)}")
        # checks if the value is 0 or negative
    if value <= 0: 
        raise ValueError(f"value cannor be 0 or negative")
    


