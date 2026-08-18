from playwright.sync_api import Page, expect

def select_data(page,is_future,target_year,target_month,target_day):
    while True:
        current_month=page.locator(".ui-datepicker-month").text_content()
        current_year=page.locator(".ui-datepicker-year").text_content()

        if current_month==target_month and current_year==target_year:
            break
        if is_future==True:
           page.locator(".ui-datepicker-next").click() # For future date
        else:
           page.locator(".ui-datepicker-prev").click() # For old data

    all_date=page.locator(".ui-datepicker-calendar td").all()
    # Selecting date from the date picker
    for dt in all_date:
        date_text=dt.inner_text()
        if date_text==target_day:
            dt.click()
            break


def test_jquery_datepicker(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")
    date_input=page.locator("#datepicker")

    #approch 1
    #date_input.fill("10/15/2022")  #mm/dd/yyyy


    #approch 2
    is_future=False
    year="2024"
    month="October"
    day="15"
    date_input.click()
    select_data(page,is_future,year,month,day)
    print("Selected data=>",date_input.inner_text())
    expect(date_input).to_have_value("10/15/2024")
    page.wait_for_timeout(5000)




    page.wait_for_timeout(3000)