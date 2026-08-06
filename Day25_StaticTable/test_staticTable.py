from playwright.sync_api import Page, expect

def test_staticWebTable(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    table=page.locator("table[name=BookTable] tbody")
    expect(table).to_be_visible()

    #1. count number of rows in a table
    rows=table.locator("tr")
    expect(rows).to_have_count(7)
    print("number of rows in a table",rows.count())

    #2. count the number th in the table
    column=rows.locator("th")
    expect(column).to_have_count(4)
    column.count()

    #3. Read all the data from the 2nd row of the table
    Second_row_cells=rows.nth(2).locator("td")
    second_row_text=Second_row_cells.all_inner_texts()
    print("Second row data ====> ",second_row_text)

    expect(Second_row_cells).to_have_text(['Learn Java', 'Mukesh', 'Java', '500'])

    print("printing 2nd row data ====> ")
    for text in second_row_text:
        print(text)

    #4. Reed all rows from the table excluding header

    all_Row_data=rows.all()
    print("printing all data from all the row and column")
    for row in all_Row_data[1:]:
        cols=row.locator("td").all_inner_texts()
        print(cols)

    #5. print book names whose author is 'mukesh'

    for row in all_Row_data[1:]:
        author_name=row.locator("td").nth(1).inner_text()
       # print(author_name)
        if author_name=="Mukesh":
            print("Book name writen by mukesh : ",row.locator("td").nth(0).inner_text())

    #6. calculate the total price of column
    total_price=0
    for row in all_Row_data[1:]:
        price=row.locator("td").nth(3).inner_text()
        total_price+=int(price)
    print("total price of book =",total_price)
