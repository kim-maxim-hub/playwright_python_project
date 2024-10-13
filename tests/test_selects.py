from playwright.sync_api import Page


def test_select(page: Page):
    page.goto('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html')
    page.locator('#sorter').first.select_option('Price')
    