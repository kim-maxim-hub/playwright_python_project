from playwright.sync_api import Page, BrowserContext, expect

def test_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/link')
    with context.expect_page() as new_tab_event:
        page.get_by_role('link', name='New page will be opened on a new tab').click()
        new_tab = new_tab_event.value        
    expect(new_tab.get_by_text('I am a new page in a new tab')).to_be_visible()
    