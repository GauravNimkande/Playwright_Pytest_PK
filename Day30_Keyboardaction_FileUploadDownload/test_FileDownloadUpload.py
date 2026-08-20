from email import message

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.skip
def test_upload_singleFile(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Uploading single file
    page.wait_for_timeout(2000)
    page.locator("#singleFileInput").set_input_files("Upload\Test1.txt")
    page.locator("button:has-text('Upload Single File')").click()

    messageElement=page.locator("#singleFileStatus")
    expect(messageElement).to_contain_text("Test1.txt")

    print("Success")
    page.wait_for_timeout(5000)


def test_upload_MultipuleFile(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # Uploading multipule file
    page.wait_for_timeout(2000)
    files=["Upload\Test1.txt","Upload\Test2.txt"]
    page.locator("#multipleFilesInput").set_input_files(files)

    page.locator("button:has-text('Upload Multiple Files')").click()

    messageElement=page.locator("#multipleFilesStatus")
    expect(messageElement).to_contain_text("Test1.txt")
    expect(messageElement).to_contain_text("Test2.txt")

    print("Success")
    page.wait_for_timeout(5000)