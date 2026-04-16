class LoginPage:
    def __init__(self, page):
        self.page = page
        self.form_auth_link = page.get_by_role('link', name="Form Authentication")
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.get_by_role("button", name="Login")
        self.logout_button = page.get_by_role("link", name="Logout")

    def login(self, username, password):
        self.form_auth_link.click()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()


    def logout(self):
        self.logout_button.click()
        self.page.wait_for_url("**/login**")

    def is_logged_in(self):
        return "/secure" in self.page.url

    def is_logged_out(self):
        return "/login" in self.page.url
