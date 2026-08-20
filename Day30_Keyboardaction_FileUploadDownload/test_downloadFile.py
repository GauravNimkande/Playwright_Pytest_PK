import os

import pytest
from playwright.sync_api import Page, expect


def test_downloadFile(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

    page.locator("#inputText").fill("Welcome")
    page.locator("#generateTxt").click()

    # regester and event
    # Approch 1
    # def handle_download(download):
    #     download.save_as("download/testfile.txt")
    #
    # page.on("download", handle_download)

    # Approch2 using lambda
    page.on("download", lambda download: download.save_as("Day30_Keyboardaction_FileUploadDownload/download/testfile.txt"))
    page.locator("#txtDownloadLink").click()

    if os.path.exists("Day30_Keyboardaction_FileUploadDownload/download/testfile.txt"):
       print("File exists")
    else:
        print("File not exists")

    page.wait_for_timeout(5000)


