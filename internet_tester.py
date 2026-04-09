from playwright.sync_api import sync_playwright

URL = "https://the-internet.herokuapp.com/"


def navigate_to_example(page, example_name: str) -> str:
    page.locator(f"text={example_name}").click()
    page.wait_for_url("**/login**")
    return page.url


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL)

        # 26x01
        assert "The Internet" in page.title(), "Title не содержит 'The Internet'"
        heading = page.get_by_role("heading", name="Available Examples")
        assert (
            heading.text_content() == "Available Examples"
        ), "Заголовок страницы не найден"
        text = heading.text_content()
        print(f"✅ Сайт доступен. Заголовок: {text}")

        # 26x02
        current_url = navigate_to_example(page, "Form Authentication")
        assert "/login" in current_url, "URL не содержит /login"
        print(f"✅ Перешли в: Form Authentication | URL: {current_url}")

        # 26x03
        # page.goto(URL)
        # page.get_by_role('link', name="Form Authentication").click()
        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("SuperSecretPassword!")
        page.get_by_role("button", name="Login").click()
        page.wait_for_url("**/secure**")
        assert "/secure" in page.url
        print("✅ Успешный вход! URL: /secure")

        # 26x04
        page.get_by_role("link", name="Logout").click()
        page.wait_for_url("**/login**")
        assert "/login" in page.url
        print(f"✅ Успешный выход! URL: {page.url}")

        # 26x05
        page.goto(URL)
        page.get_by_role("link", name="Checkboxes").click()
        page.wait_for_url("**/checkboxes", timeout=30000)
        checkbox1 = page.locator("input[type='checkbox']").nth(0)
        checkbox2 = page.locator("input[type='checkbox']").nth(1)
        assert not checkbox1.is_checked()
        assert checkbox2.is_checked()
        checkbox1.check()
        checkbox2.uncheck()
        assert checkbox1.is_checked()
        assert not checkbox2.is_checked()
        assert "/checkboxes" in page.url

        # 26x06
        page.goto(URL)
        page.get_by_role("link", name="Dropdown").click()
        page.wait_for_url("**/dropdown")
        dropdown = page.locator("#dropdown")
        # dropdown.select_option("#dropdown")
        assert (
            dropdown.locator("option:checked").text_content()
            == "Please select an option"
        )
        dropdown.select_option(label="Option 1")
        assert dropdown.locator("option:checked").text_content() == "Option 1"
        dropdown.select_option(label="Option 2")
        assert dropdown.locator("option:checked").text_content() == "Option 2"
        print("✅ Выбрано: Option 2")

        # 26x07
        page.goto(URL)
        page.get_by_role("link", name="Inputs").click()
        numbers_input = page.locator("input[type='number']")
        page.wait_for_url("**/inputs")
        numbers_input.fill("123")
        assert numbers_input.input_value() == "123"
        numbers_input.clear()
        assert numbers_input.input_value() == ""
        numbers_input.fill("456")
        assert numbers_input.input_value() == "456"
        print("✅ Введено: 456")

        # 26x08
        page.goto(URL)
        page.get_by_role("link", name="Hovers").click()
        figure = page.locator(".figure").nth(0)
        figure.hover()
        text = figure.locator("h5")
        assert text.is_visible()
        print("✅ Навели на изображение. Текст: name: user1")

        # 26x09
        page.goto(URL)
        page.get_by_role("link", name="JavaScript Alerts").click()
        page.wait_for_url("**/javascript_alerts")
        page.once("dialog", lambda dialog: dialog.accept())
        page.get_by_role("button", name="Click for JS Alert").click()
        result = page.locator("#result")
        assert result.text_content() == "You successfully clicked an alert"
        print("✅ Alert принят. Сообщение: You successfully clicked an alert")

        # 26x10
        page.goto(URL)
        page.get_by_role("link", name="File Upload").click()

        browser.close()
