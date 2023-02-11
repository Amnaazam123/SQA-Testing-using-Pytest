# scope="function" is a default scope which is run before each test function, not matter from what class it belongs to...

import pytest

@pytest.fixture(scope="function")
def fixture():
    print("setup")
    yield 10
    print("teardown")

class TestClass1:
    def test_method1(self,fixture):
        print("testclass1_method1")
        assert fixture == 10

    def test_method2(self,fixture):
        print("testclass1_method2")
        assert fixture == 10
        
    def test_method3(self,fixture):
       print("testclass1_method3")
       assert fixture == 10
       
       
class TestClass2:
    def test_method1(self,fixture):
        print("testclass2_method1")
        assert fixture == 10

    def test_method2(self,fixture):
        print("testclass2_method2")
        assert fixture == 10
        
    def test_method3(self,fixture):
       print("testclass2_method3")
       assert fixture == 10


# output:
      # temp.py setup
      # testclass1_method1
      # teardown
      # setup
      # testclass1_method2
      # teardown
      # setup
      # testclass1_method3
      # teardown
      # setup
      # testclass2_method1
      # teardown
      # setup
      # testclass2_method2
      # teardown
      # setup
      # testclass2_method3
      # teardown
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# scope="class" is a scope in which run fixture runs only before the test functions of one class.

import pytest

@pytest.fixture(scope="class")
def fixture():
    print("setup")
    yield 10
    print("teardown")

class TestClass1:
    def test_method1(self,fixture):
        print("testclass1_method1")
        assert fixture == 10

    def test_method2(self,fixture):
        print("testclass1_method2")
        assert fixture == 10
        
    def test_method3(self,fixture):
       print("testclass1_method3")
       assert fixture == 10
       
       
class TestClass2:
    def test_method1(self,fixture):
        print("testclass2_method1")
        assert fixture == 10

    def test_method2(self,fixture):
        print("testclass2_method2")
        assert fixture == 10
        
    def test_method3(self,fixture):
       print("testclass2_method3")
       assert fixture == 10

# output:
        # setup
        # testclass1_method1
        # testclass1_method2
        # testclass1_method3
        # teardown
        # setup
        # testclass2_method1
        # testclass2_method2
        # testclass2_method3
        # teardown


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# A module scope fixture is shared among all tests within a single module(single file), not depending upon class or function.
import pytest

@pytest.fixture(scope="module")
def fixture():
    print("setup")
    yield 10
    print("teardown")

class TestClass1:
    def test_method1(self,fixture):
        print("testclass1_method1")
        assert fixture == 10

    def test_method2(self,fixture):
        print("testclass1_method2")
        assert fixture == 10
        
    def test_method3(self,fixture):
       print("testclass1_method3")
       assert fixture == 10
       
       
class TestClass2:
    def test_method1(self,fixture):
        print("testclass2_method1")
        assert fixture == 10

    def test_method2(self,fixture):
        print("testclass2_method2")
        assert fixture == 10
        
    def test_method3(self,fixture):
       print("testclass2_method3")
       assert fixture == 10

# output:
        # setup
        # testclass1_method1
        # testclass1_method2
        # testclass1_method3
        # testclass2_method1
        # testclass2_method2
        # testclass2_method3
        # teardown
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# The main difference between a module and a package is that a module is a single file, while a package is a directory that contains multiple modules and other packages.
# So, the main difference between module and package scope fixtures is the level of sharing that is defined for the fixture. 
# A module scope fixture is shared among all tests within a single module, while a package scope fixture is shared among all tests within a single package.
# Session scope is the broad scope in pytest fixture :)




