import pytest

"""This will be the base class for all the test classes to use the Fixture to invoke the browser"""
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
