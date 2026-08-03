import pytest


def test_loginbyEmail():
    print("This is login by email")
    assert 1 == 1


def test_loginbyPhone():
    print("This is login by phone")
    assert 1 == 1

@pytest.mark.skip  #this we called as a decorator
def test_loginbyfacebook():
    print("This is login by facebook")
    assert 1 == 1

@pytest.mark.skip #this we called as a decorator
def test_signupbyemail():
    print("This is signup by email")
    assert True == True


def test_signupbyfacebook():
    print("This is signup by facebook")
    assert True == True

@pytest.mark.skip   #this we called as a decorator
def test_signupbyphone():
    print("This is signup by phone")
    assert True == True
