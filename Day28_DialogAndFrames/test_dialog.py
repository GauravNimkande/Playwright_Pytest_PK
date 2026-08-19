from tkinter import dialog

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.skip
def test_simple_dilog(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)

    # Approch 1
    # ==========  regestaring an event  =========================
    def handel_dialog(dialog):
        dialog.accept()

    page.on("dialog",handel_dialog)
    #=============================================

    page.locator("#alertBtn").click() #clicking on the button

    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_simple_dilog2(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)


    # ===== Approch 2 ===================
    page.on("dialog", lambda dialog: dialog.accept()) # lambda parameter : expression
    # =============================================

    page.locator("#alertBtn").click()  # clicking on the button

    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_confermation_dilog(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)


    # ===== Approch 2 ===================
   # page.on("dialog", lambda dialog: dialog.accept()) # lambda parameter : expression
    page.on("dialog", lambda dialog: dialog.dismiss())  # lambda parameter : expression

    # =============================================

    page.locator("#confirmBtn").click()  # clicking on the button
    #page.wait_for_selector("#demo")
    page.wait_for_timeout(6000)
    #expect(page.locator("#demo")).to_have_text("You pressed OK!")
    expect(page.locator("#demo")).to_have_text("You pressed Cancel!")

    page.wait_for_timeout(2000)


def test_prompt_dialog(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)

    # ===== Approch 2 ===================
   # page.on("dialog", lambda dialog: dialog.accept()) # lambda parameter : expression
    page.on("dialog", lambda dialog: dialog.accept('John'))  # lambda parameter : expression

    # =============================================

    page.locator("#promptBtn").click()  # clicking on the button

    text= page.locator("#demo").inner_text()
    print("Output text", text)

    expect(page.locator("#demo")).to_have_text("Hello John! How are you today?")
    page.wait_for_timeout(2000)