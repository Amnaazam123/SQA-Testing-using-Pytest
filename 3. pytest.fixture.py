# A fixture is a set of setup and teardown steps that are run before and after a test function. 
# The fixture function returns a value which is passed to the test function as an argument.

import pytest

@pytest.fixture
def input_value():
  print("running fixture")
   input = 39
   return input

def test_divisible_by_3(input_value):
        print("test_divisible_by_3")
        assert input_value % 3 == 0
   
def test_divisible_by_6(input_value):
        print("test_divisible_by_6")
        assert input_value % 6 == 0    


# output:
        # running fixture
        # test_divisible_by_3
        # running fixture
        # test_divisible_by_6


# @pytest.fixture(autouse=True), the fixture is used without explicitly including it as an argument in each test function.
# You can use the -s option with pytest to print statements written in test functions: `!pytest -s fileName.py`

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import pytest

@pytest.fixture
def input_value():
   print("\nrunning fixture as setup")
   input = 39
   yield input            # it is equal to return input, before and after yield statement, all the statements are considered the part of setup and teradown respectively.
   print ("\nrunning fixture as teardown")

def test_divisible_by_3(input_value):
   print("test_divisible_by_3")
   assert input_value % 3 == 0
   
def test_divisible_by_6(input_value):
    print("test_divisible_by_6")
    assert input_value % 3 == 0 
      
# output:
        # running fixture as setup
        # test_divisible_by_3
        # running fixture as teardown

        # running fixture as setup
        # test_divisible_by_6
        # running fixture as teardown
