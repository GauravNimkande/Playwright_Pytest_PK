import pytest

'''
test_loginbyEmail --> sanity, regression
test_loginbyPhone --> regression
test_loginbyFacebook --> sanity

test_signupbyEmail --> sanity, regression
test_signupbyPhone --> sanity
test_signupbyFacebook --> regression

test_paymentindollor --> sanity, regression
test_paymentinrupees --> regression
'''

'''
1) run sanity tests : pytest  Day17_pytestfixture2/test_grouping.py -v  -s -m "sanity"
2) run regression tests : pytest  Day17_pytestfixture2/test_grouping.py -v  -s -m "regression"
3) run test which belong to sanity and regression: pytest  Day17_pytestfixture2/test_grouping.py -v  -s -m "sanity and regression"
4) run only sanity not belong to regression : pytest  Day17_pytestfixture2/test_grouping.py -v  -s -m "sanity" -m "not regression"                                                                 
'''



@pytest.mark.sanity
@pytest.mark.regression
def test_loginbyEmail():
    print("This is login by email")
    assert 1 == 1


@pytest.mark.regression
def test_loginbyPhone():
    print("This is login by phone")
    assert 1 == 1


@pytest.mark.sanity
def test_loginbyfacebook():
    print("This is login by facebook")
    assert 1 == 1


@pytest.mark.regression
@pytest.mark.sanity
def test_signupbyemail():
    print("This is signup by email")
    assert True == True


@pytest.mark.regression
def test_signupbyfacebook():
    print("This is signup by facebook")
    assert True == True


@pytest.mark.sanity
def test_signupbyphone():
    print("This is signup by phone")
    assert True == True


@pytest.mark.regression
@pytest.mark.sanity
def test_paymentindollor():
    print("This is payment indullo")
    assert True == True


@pytest.mark.regression
def test_paymentinrupees():
    print("This is payment inrupees")
    assert True == True
