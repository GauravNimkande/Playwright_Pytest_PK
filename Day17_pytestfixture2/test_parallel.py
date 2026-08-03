
'''
pre-requisites: intall a pytest plugin "pytest xdist" to run tests parallel
pip install pytest-xdist

command= pytest  Day17_pytestfixture2/test_parallel.py -v  -s -n 2
'''

def test_one():
    print("Running test_one")
    assert True==True

def test_two():
    print("Running test_two")
    assert True==True

def test_three():
    print("Running test_three")
    assert True==True

def test_four():
    print("Running test_four")
    assert True==True