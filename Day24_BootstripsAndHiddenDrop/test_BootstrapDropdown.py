from playwright.sync_api import Page, expect

def test_bootstrapDropdown(page: Page):

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("Username").fill("admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.locator("button[type='submit']").click()

    #click on PIM tab
    page.get_by_text("PIM").click()

    #click on job title dropdown
    page.locator("form i").nth(2).click() # this will open all options dropdown

    page.wait_for_timeout(3000)

    # Capture all ther opetion from the dropdown
    options=page.locator("div[role='listbox'] span")
    count=options.count()
    print("Number of dropdown options", count)

    expect(options).to_have_count(33)
    # Print all opetions from dropdown
    print("all the options from the dropdown", options.all_text_contents())

    #print all the options from the dropdown using loop
    for i in range(count):
        print(options.nth(i).text_content())

    # Select the specific option from the dropdown
    for i in range(count):
        text=options.nth(i).text_content()
        if text=="Software Architect":
            options.nth(i).click()
            break



    page.wait_for_timeout(5000)