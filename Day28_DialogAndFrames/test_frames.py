import pytest
from playwright.sync_api import Page, expect


def test_frames(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    frames=page.frames
    print("Number of frames available on page: ", len(frames))

    # frame 1 ================
    #frame1=page.frame_locator("frame[src='frame_1.html']") # First Approch
    #frame1=page.frame("name of the frame") # 3 rd approch we can use name of the frame
    frame1=page.frame(url='https://ui.vision/demo/webtest/frames/frame_1') # second approch
    frame1.locator("input[name='mytext1']").fill("Welcome to my first app")

    page.wait_for_timeout(3000)
