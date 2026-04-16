from pages.login_page import LoginPage


def test_user_can_login_and_logout(page):
    login_page = LoginPage(page)

    login_page.login("tomsmith", "SuperSecretPassword!")
    assert login_page.is_logged_in()
    print("✅ Успешный вход! URL: /secure")

    login_page.logout()
    assert login_page.is_logged_out()
    print(f"✅ Успешный выход! URL: {page.url}")