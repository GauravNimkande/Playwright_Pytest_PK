# fixture : reusable function
import pytest


@pytest.fixture
def setupBrowser():
    print(".... Setup browser")

def test_one(setupBrowser):
    print("this is my test one")

def test_two(setupBrowser):
    print("this is my test two")

def test_three(setupBrowser):
    print("this is my test ")