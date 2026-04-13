from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/")

    # 27x06
    text = page.get_by_role("heading", name="Available Examples").inner_text()
    print(text)
    expect(page.get_by_role("heading", name="Available Examples")).to_contain_text("Available Examples")

    # 27x07
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith2")
    page.locator("#password").fill("SuperSecretPassword!!")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("#flash")).to_contain_text("Your username is invalid!")