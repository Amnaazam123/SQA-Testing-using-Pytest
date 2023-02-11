import pytest

# you can mark tests with any label like `mymarker`, so that you can run only those test which are marked with 'mymarker' 
@pytest.mark.mymarker
def test_send_http():
    pass  #  the test functions are defined, but the actual test code is not yet written. The pass statement is used as a placeholder until the test code is written.


def test_something_quick():
    pass


def test_another():
    pass


class TestClass:
    def test_method(self):
        pass


# If you want to test/run only those functions which are marked with your defined label,
# write command `!pytest -m markerName fileName.py`
# This command will run only those testcases which are marked with 'markerName'.
# If you want to run testcases that do not belong to `markerName` mark,
# You will use command `!pytest -m "not markerName" fileName.py`
