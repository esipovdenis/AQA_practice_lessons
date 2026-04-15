import pytest
from playwright.sync_api import sync_playwright

URL = "https://the-internet.herokuapp.com/"


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL)
        yield page
        browser.close()