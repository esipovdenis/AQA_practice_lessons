class CheckboxesPage:
    def __init__(self, page):
        self.page = page
        self.checkbox_link = self.page.get_by_role("link", name="Checkboxes")
        self.checkboxes = self.page.locator("input[type='checkbox']")


    def open(self):
        self.checkbox_link.click()
    #
    # def first_checkbox(self):
    #     return self.checkboxes.nth(0)
    #
    # def second_checkbox(self):
    #     return self.checkboxes.nth(1)
    #
    # def is_first_checked(self):
    #     return self.first_checkbox().is_checked()
    #
    # def is_second_checked(self):
    #     return self.second_checkbox().is_checked()

    def set_checkboxes(self):
        self.checkboxes.nth(0).check()
        self.checkboxes.nth(1).uncheck()

    def has_expected_state(self):
        return self.checkboxes.nth(0).is_checked() and not self.checkboxes.nth(1).is_checked()


        page.goto(URL)
        self.checkbox_link.click()
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