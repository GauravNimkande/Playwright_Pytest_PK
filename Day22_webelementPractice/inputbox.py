import pytest
from playwright.sync_api import Playwright,expect, Page

def test_inputbox(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    text_box=page.locator("#name")
    #visibility of the element and emable or not
    expect(text_box).to_be_visible()
    expect(text_box).to_be_enabled()

    #check the attribute of the element
    expect(text_box).to_have_attribute("maxlength","15")
    maxlenmth=text_box.get_attribute("maxlength")

    #fill the text in textbox
    text_box.fill("abc")

    #get the value from input box
    entered_value=text_box.input_value()
    print("entered_value",entered_value)

    page.wait_for_timeout(5000)