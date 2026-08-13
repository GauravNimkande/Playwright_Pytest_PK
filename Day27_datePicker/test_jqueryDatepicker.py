from playwright.sync_api import Page, expect

def select_data(page,date_input,is_future,target_year,target_month,target_day):
    while True:
        current_month=page.locator(".ui-datepicker-month").text_content()
        current_year=page.locator(".ui-datepicker-year").text_content()

        if current_month==target_month and current_year==target_year:
            break
        if is_future==True:
           page.locator(".ui-datepicker-next").click() # For future date
        else:
           page.locator(".ui-datepicker-prev").click()

def test_jquery_datepicker(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")
    date_input=page.locator("#datepicker")

    #approch 1
    #date_input.fill("10/15/2022")  #mm/dd/yyyy


    #approch 2
    is_future=True
    year="2025"
    month="12"
    day="10"
    date_input.click()
    select_data(page,date_input,is_future,year,month,day)




    page.wait_for_timeout(3000)