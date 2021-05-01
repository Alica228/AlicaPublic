import os
import time
from pets.pages.elements import WebElement
from pets.pages.base import WebPage


class AuthPage(WebPage):

    def __init__(self, driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "http://petfriends1.herokuapp.com/login"
        super().__init__(driver, url)

    email = WebElement(id="email")
    passw = WebElement(id="pass")
    btn = WebElement(class_name="btn-success")

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_pass(self, value):
        self.passw.send_keys(value)

    def btn_click(self):
        self.btn.click()
