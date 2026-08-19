import pytest
from playwright.sync_api import Page, expect

pytest.mark.skip
def test_mouse_hover(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    pointmebtn=page.locator("button[class='dropbtn']")
    pointmebtn.hover()
    page.wait_for_timeout(2000)
    laptop=pointmebtn.locator(".dropdown-content a:nth-child(2)") # alos we can use direct css ".dropdown-content a:nth-child(2)"
    laptop.hover()

    #for right click
    laptop.click(button="right")

    page.wait_for_timeout(3000)

pytest.mark.skip
def test_dobbelClick(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.locator("#field1").fill("Hello")

    btncopy=page.locator("button[ondblclick='myFunction1()']")
    btncopy.dblclick() #perform doubleclick

    expect(page.locator("#field2")).to_have_value("Hello")

    page.wait_for_timeout(3000)


def test_DragAndDrop(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    sorce=page.locator("#droppable")
    targer=page.locator("#droppable")


    #Approch1: Manual drag and drop
    # sorce.hover()
    # page.mouse.down()
    # targer.hover()
    # page.mouse.up()

    #Approch 2:  drag_to()
    sorce.drag_to(targer)

    page.wait_for_timeout(3000)