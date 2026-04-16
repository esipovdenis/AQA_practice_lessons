from pages.checkboxes_page import CheckboxesPage


def test_checkboxes(page):
    checkboxes_page = CheckboxesPage(page)

    checkboxes_page.open()
    checkboxes_page.set_checkboxes()
    assert checkboxes_page.has_expected_state()