from .pages.login_page import LoginPage

link_login = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


def test_guest_should_see_login_url(browser):
    page = LoginPage(browser, link_login)
    page.open()
    page.should_be_login_url()

def test_guest_should_see_login_form(browser):
    page = LoginPage(browser, link_login)
    page.open()
    page.should_be_login_form()

def test_guest_should_see_register_form(browser):
    page = LoginPage(browser, link_login)
    page.open()
    page.should_be_register_form()


# pytest -v --tb=line --language=en test_login_page.py
