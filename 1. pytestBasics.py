#Pytest considers any function with a name that starts with "test" to be a test function.
# Define the functions with test as prefix of function name and assert the conditions inside them.

import pytest
def area_of_rectangle(width, height):
    area = width*height
    return area 
    
def perimeter_of_rectangle(width, height):
    perimeter = 2 * (width + height)
    return perimeter

def test_area():
    output = area_of_rectangle(2,5)
    assert output == 10
 
def test_perimeter():
    output = perimeter_of_rectangle(2,5)
    assert output == 14
    
# To run this file, write command `!pytest fileName.py`
