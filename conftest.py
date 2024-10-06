import pytest


@pytest.fixture(scope="function")
def browser_context_args(browser_context_args):
    return {
      
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }
    
# from playwright.sync_api import sync_playwright


# @pytest.fixture
# def browser_fixture():
#     with sync_playwright() as playwright:
#         browser = p.chromium.launch(headless=False,
#         args=["--start-maximized", 
#         "--disable-blink-features=AutomationControlled",
#         "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) "
#             "Chrome/120.0.0.0 Safari/537.36s"
#         ]
#         )
#         context = browser.new_context()
#         page = context.new_page()
#         yield page
#         page.close()
#         browser.close()
