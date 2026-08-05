from playwright.sync_api import Page, expect

def test_pwmethords(page: Page):

    page.goto("https://demowebshop.tricentis.com/")
    products=page.locator(".product-title")

    # 1) inner_text() vs text_content()

    # print("Using inner_text()=",products.nth(1).inner_text()) # return actual text
    # print("Using text_content()=",products.nth(1).text_content()) # return content with special char and spaces

    # count=products.count()
    # for i in range(count):
    #    # print(products.nth(i).inner_text())
    #     print(products.nth(i).text_content())

    #2) all_inner_texts() vs all_text_contents()

    #product_name=products.all_inner_texts() # you will get all exact product name
    #print(product_name)

    # product_name = products.all_text_contents()  # you will get all product name with /n spectial char and spaces
    # print(product_name)

    #3) all()
    product_name=products.all()
    print(product_name[0].inner_text())