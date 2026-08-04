from playwright.sync_api import Page, expect

def test_single_select_dropdown(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    # 3 ways select option from dropdown

    #page.locator("#country").select_option("India") # By lable

    #page.locator("#country").select_option("uk") # By Value

    page.locator("#country").select_option(index=5) # By index

    #Check number of options in dropdown
    dropdown_opetionsCount=page.locator("#country>option")
    expect(dropdown_opetionsCount).to_have_count(10)
    page.wait_for_timeout(5000)