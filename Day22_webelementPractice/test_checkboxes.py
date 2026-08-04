from calendar import weekday

from playwright.sync_api import Playwright, expect, Page


def test_checkbox(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # 1. Select the specific checkbnox
    Sunday_CheckBox = page.get_by_label("Sunday")

    Sunday_CheckBox.check()

    expect(Sunday_CheckBox).to_be_checked()

    # 2. count number of checkboxes

    # Step 1:
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    checkboxes = []

    # Step 2:
    # for day in days:
    #     checkbox=page.get_by_label(day).click()
    #     checkboxes.append(checkbox)

    # insted of above we can use below code as well more optimize

    checkboxes = [page.get_by_label(day) for day in days]
    print("Total checkboxes: ", len(checkboxes))

    # Step 3: Select all the checkboxes and assert each checkbox is selected

    # for checkbox in checkboxes:
    #     checkbox.check()
    #     expect(checkbox).to_be_checked()
    #
    # page.wait_for_timeout(3000)

    # Step 4 un check last 3 check boxes

    # for checkbox in checkboxes[-3:]:
    #     checkbox.uncheck()
    #     expect(checkbox).not_to_be_checked()
    #
    # page.wait_for_timeout(3000)

    # Step 5: Toggle checkboxes

    # for checkbox in checkboxes:
    #     if checkbox.is_checked():
    #         checkbox.uncheck()
    #         expect(checkbox).not_to_be_checked()
    #     else:
    #         checkbox.check()
    #         expect(checkbox).to_be_checked()


    page.wait_for_timeout(3000)


    # step 6: Randomly check checkboxes - check 1,3,6 checkboxes

    index=[1,3,6]

    for i in index:
        checkboxes[i].check()
        expect(checkboxes[i]).to_be_checked()

    page.wait_for_timeout(3000)

    # Step 7: Select check boxes based on the lable/input value
    weekday="Friday"
    for lable in days:
        if lable == weekday:
            checkboxe=page.get_by_label(lable)
            checkboxe.check()
            expect(checkboxe).to_be_checked()
    page.wait_for_timeout(3000)