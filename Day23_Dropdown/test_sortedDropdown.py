from playwright.sync_api import Page, expect

def test_Multi_select_dropdown(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

   # dropdownoption=page.locator("#colors>option")  #Unsorted List

    dropdownoption=page.locator("#animals>option") # sorted list

    option_text=[text.strip() for text in dropdownoption.all_text_contents()]
    orignalList=option_text.copy()

    sortedList=sorted(orignalList)

    print(orignalList)
    print(sortedList)

    if orignalList==sortedList:
        print("Dropdown options are Sorted order")
    else:
        print("Dropdown options are Not Sorted order")

    page.wait_for_timeout(5000)