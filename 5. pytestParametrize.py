import pytest
def cal_square(num):
    return num * num

# # Test case 1
def test_cal_square_1():
    result = cal_square(5)
    assert result == 25
 
 
# Test case 2
def test_cal_square_2():
    result = cal_square(6)
    assert result == 36
 
 
# Test case 3
def test_cal_square_3():
    result = cal_square(7)
    assert result == 49
 
 
# Test case 4
def test_cal_square_4():
    result = cal_square(8)
    assert result == 64

# The code for the test cases is the same except for the input. To get rid of such things, we will perform parameterization.

#-----------------------------------------------------------------------SOLUTION--------------------------------------------
@pytest.mark.parametrize("myInput, output",[(5,25),(4,16),(10,100)])
def test_cal_square(myInput,output):
    assert cal_square(myInput) == output
    
    
    
