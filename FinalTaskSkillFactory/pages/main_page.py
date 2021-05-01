#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os
import time
from pages.base import WebPage
from pages.elements import WebElement



class MainPage(WebPage):

    def __init__(self, driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://www.e-katalog.ru/"
        super().__init__(driver, url)

    def register_user(self, name, email, password):
        enter_button = WebElement(_class="wu_entr")
        enter_button.click()

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_pass(self, value):
        self.passw.send_keys(value)

    def btn_click(self):
        self.btn.click()
