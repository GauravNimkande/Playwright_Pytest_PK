from playwright.sync_api import Page, expect

def test_verify_paginationTable(page: Page):

    page.goto("https://datatables.net/examples/core/basic_init/zero_configuration.html")
    has_more_pages=True
    while has_more_pages:
        rows=page.locator("#example tbody tr").all()
        for row in rows:
            print(row.inner_text())

        nextPage=page.locator("button[aria-label='Next']")
        is_disabled=nextPage.get_attribute("class")
        if "disabled" in is_disabled:
            has_more_pages=False
        else:
            nextPage.click()
    page.wait_for_timeout(5000)


def test_filter_rows(page: Page):
    page.goto("https://datatables.net/examples/core/basic_init/zero_configuration.html")
    dropdown=page.locator("#dt-length-0")
    dropdown.select_option(label="25")

    rows = page.locator("#example tbody tr") #it will return

    expect(rows).to_have_count(25)
