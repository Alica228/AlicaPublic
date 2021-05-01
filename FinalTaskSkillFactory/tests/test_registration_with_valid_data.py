from pages.main_page import MainPage
import pytest
import time


def test_auth_page(web_browser):
    page = MainPage(web_browser)

    page.register_user()

    time.sleep(1)

