from playwright.sync_api import Page


def test_iframe(page: Page):
    page.goto('https://www.qa-practice.com/elements/iframe/iframe_page')
    page.frame_locator('iframe').locator('.navbar-toggler-icon').click()
    