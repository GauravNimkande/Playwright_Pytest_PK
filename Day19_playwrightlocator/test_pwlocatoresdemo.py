import time

from playwright.sync_api import Page, expect

def test_verify_pwlocator(page:Page):
    page.goto("https://practicetestautomation.com/practice-test-login/")

    # 1. page.get_by_alt_text()
    logo=page.get_by_alt_text("Practice Test Automation")
    expect(logo).to_be_visible()
    time.sleep(5)

    # 2. page.get_by_text()
    page.get_by_text("Home").is_visible()

    #3. page.get_by_role
   # page.get_by_role("textbox",name="username").click()
    page.get_by_role("textbox", name="username").fill("student")


    #4. page.get_by_lable()
    page.get_by_label("Password").fill("Password123")
    

    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    page.get_by_placeholder("Enter your full name").fill("Gaurav")


    #6  page.get_by_title()
    expect(page.get_by_title("Home page link")).to_have_text("Home")
    time.sleep(5)
