import time

import playwright
from playwright.sync_api import Page, expect
'''
tag id              -->  tag#id
tag class           -->  tag.class
tag attribute       --> tag[attribute=value]
tag class attribute --> tag.class[attribute=value]

'''


def test_verify_css_locator(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    # tag id (tag name is optional)
    #page.locator("input#small-searchterms").fill("T-Shirts")
    #page.locator("#small-searchterms").fill("T-Shirts")
    #time.sleep(5)

    # tag class (tag is optional)
    #page.locator("input.search-box-text").fill("T-Shirts")
    #page.locator(".search-box-text").fill("T-Shirts")
    #time.sleep(5)

    # tag attribute       --> tag[attribute=value]
    #page.locator("input[name=q]").fill("T-Shirts")
    #page.locator("[name=q]").fill("T-Shirts")
    #time.sleep(5)

    # tag class attribute --> tag.class[attribute=value]
    #page.locator("input.search-box-text[value='Search store']").fill("T-Shirts")
    page.locator(".search-box-text[value='Search store']").fill("T-Shirts")
    time.sleep(5)