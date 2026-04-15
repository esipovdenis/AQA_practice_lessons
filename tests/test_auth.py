from pages.login_page import LoginPage


def test_user_can_login_and_logout(page):
    login_page = LoginPage(page)

    login_page.login("tomsmith", "SuperSecretPassword!")
    page.wait_for_url("**/secure**")
    assert "/secure" in page.url
    print("✅ Успешный вход! URL: /secure")

    login_page.logout()
    assert "/login" in page.url
    print(f"✅ Успешный выход! URL: {page.url}")