from playwright.sync_api import sync_playwright

URL = "https://the-internet.herokuapp.com/"


def navigate_to_example(page, example_name: str) -> str:
    page.locator(f"text={example_name}").click()
    page.wait_for_url("**/login**")
    return page.url


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()
        page.goto(URL)

        # 26x01
        assert "The Internet" in page.title(), "Title не содержит 'The Internet'"
        heading = page.get_by_role("heading", name="Available Examples")
        assert heading.text_content() == "Available Examples", "Заголовок страницы не найден"
        text = heading.text_content()
        print(f"✅ Сайт доступен. Заголовок: {text}")

        # 26x02
        current_url = navigate_to_example(page, "Form Authentication")
        assert "/login" in current_url, "URL не содержит /login"
        print(f"✅ Перешли в: Form Authentication | URL: {current_url}")

        browser.close()