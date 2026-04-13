from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://demoqa.com/buttons")

    #27x01
    text = page.locator("#doubleClickBtn").inner_text()
    assert text == "Double Click Me"
    print(f"✅ {text}")

    # 27x02
    page.get_by_role("button", name="Click Me", exact=True).click()
    expect(page.locator("#dynamicClickMessage")).to_have_text("You have done a dynamic click")
    text = page.locator("#dynamicClickMessage").inner_text()
    assert "You have done a dynamic click" in text
    print(f"✅ {text}")

    # 27x03
    page.locator("#item-0").click()
    page.locator("#userName").fill("Denis")
    page.locator("#userEmail").fill("denis@eample.com")
    name = page.locator("#userName").input_value()
    email = page.locator("#userEmail").input_value()
    print(f"Имя: {name}, Email: {email}")

    # 27x04
    page.goto("https://demoqa.com/select-menu")
    options = page.locator("#oldSelectMenu option").all_inner_texts()
    print(options)
    assert "Red" in options

    # 27x05
    page.goto("https://demoqa.com/text-box")
    address = page.locator("#currentAddress-label")
    text1 = address.inner_text()
    text2 = address.text_content()
    print(repr(text1))
    print(repr(text2))




