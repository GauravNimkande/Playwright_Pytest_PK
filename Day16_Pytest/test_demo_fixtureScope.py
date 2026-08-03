import pytest

#fixture="function" : fixture will be called before every test function executed
#fixture="module" : fixture will be called before only once before test function executed
#fixture="class" : fixture will be called only once before the class
#fixture="session" : fixture will be called only once for session


@pytest.fixture(scope="module")
def setupBrowser():
    print(".... Setup browser")

def test_one(setupBrowser):
    print("this is my test one")

def test_two(setupBrowser):
    print("this is my test two")

def test_three(setupBrowser):
    print("this is my test ")