import pytest
from playwright.sync_api import Page, expect


def test_keyboardAction(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    input1=page.locator("#input1")
    #1. focus on input1
    input1.focus()

    # provide the text in input1
    page.keyboard.insert_text("Welcome")
    # press cnt A
    page.keyboard.press("Control+A")
    page.keyboard.press("Control+C")

    # press tab key 2 times to navigate / focuse on input2
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    # to press the text in input 2
    page.keyboard.press("Control+V")

    # press tab key 2 times to navigate / focuse on input3
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    # to press the text in input 3
    page.keyboard.press("Control+V")

    input2 = page.locator("#input2")
    input3 = page.locator("#input3")

    expect(input2).to_have_value("Welcome")
    expect(input3).to_have_value("Welcome")

    page.wait_for_timeout(5000)