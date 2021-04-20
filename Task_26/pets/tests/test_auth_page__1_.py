from pages.auth_page import AuthPage
import time


def test_auth_page(web_browser):
    page = AuthPage(web_browser)

    page.enter_email('email@gmail.com')
    page.enter_pass('pass')
    page.btn_click()

    assert page.get_relative_link() != '/all_pets', 'авторизация не удалась'

    time.sleep(5)

