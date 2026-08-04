from playwright.sync_api import Playwright,expect, Page

def test_radioButton(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    male_radio=page.locator("#male")

    #check visiblity of the element and enable or not
    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled()

    #male radio button should not be checked by default
    expect(male_radio).not_to_be_checked()

    # Select/check radio buttion action
    male_radio.check()
    expect(male_radio).to_be_checked()
    page.wait_for_timeout(5000)



