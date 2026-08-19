from playwright.sync_api import Page, expect


def test_iframes(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    # frame 3
    frame3 = page.frame(url='https://ui.vision/demo/webtest/frames/frame_3') # it will grape the frame 3
    frame3.locator("input[name='mytext3']").fill("Welcome")

    # count how many inner frame is there
    child_frames=frame3.child_frames
    print("Number of child frames: ", len(child_frames))

    innerFrame=child_frames[0]
    radiobtn=innerFrame.get_by_label("I am a human")
    radiobtn.check()
    expect(radiobtn).to_be_checked()
    page.wait_for_timeout(3000)
