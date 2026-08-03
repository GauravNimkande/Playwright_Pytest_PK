'''
pre-requisites: install pytest-order plugin
command: pip install pytest-order
'''
import pytest


# 1st approch : order test by position
# @pytest.mark.order(1)
# def test_login():
#     print("this is login test")
#
# @pytest.mark.order(3)
# def test_add_item():
#     print("this is add item test")
# @pytest.mark.order(2)
# def test_logout():
#     print("this is logout test")


# 2nd approch using before, after
#
# @pytest.mark.order(1)
# def test_login():
#     print("this is login test")
#
#
# @pytest.mark.order()
# def test_add_item():
#     print("this is add item test")
#
#
# @pytest.mark.order(before="test_add_item")
# def test_logout():
#     print("this is logout test")

# 3rd approch using marker string

@pytest.mark.order("first")
def test_login():
    print("this is login test")


@pytest.mark.order()
def test_add_item():
    print("this is add item test")


@pytest.mark.order("last")
def test_logout():
    print("this is logout test")