class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.get_by_role('link', name="Form Authentication").click()
        self.page.locator("#username").fill(username)
        self.page.locator("#password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def logout(self):
        self.page.get_by_role("link", name="Logout").click()
        self.page.wait_for_url("**/login**")
