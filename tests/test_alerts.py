from playwright.sync_api import Page, Dialog

def test_alert(page: Page):
    page.goto('https://www.demoblaze.com/')

    def accept_alert(alert: Dialog):
        print(alert.message)
        alert.accept()

    page.on('dialog', accept_alert)
    page.get_by_role('link', name='Samsung galaxy s6').click()
    page.get_by_role('link', name='Add to cart').click()
    page.wait_for_event('dialog')
    page.locator('#cartur').click()
