from playwright.sync_api import Page, expect

def test_Multi_select_dropdown(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    # select multiple values from the dropdown

    #page.locator("#colors").select_option(["Blue", "Yellow", "White"]) # By Using lable

    #page.locator("#colors").select_option(value=["red", "yellow", "green"]) # By Using Value

    #page.locator("#colors").select_option(index=[3,2,5])  # By Using index

    MultiDropDownOptions=page.locator("#colors>option")
    expect(MultiDropDownOptions).to_have_count(7)

    page.wait_for_timeout(5000)