import pytest

#fixture="function" : fixture will be called before every test function executed
#fixture="module" : fixture will be called before only once before test function executed
#fixture="class" : fixture will be called only once before the class
#fixture="session" : fixture will be called only once for session


@pytest.fixture(scope="module")
def setupBrowser():
    print(".... Setup browser")
    return "chrome"



def test_one(setupBrowser):
    print("this is my test one")
    print("browser is: "+setupBrowser)


def test_two():
    print("this is my test two")

def test_three():
    print("this is my test ")