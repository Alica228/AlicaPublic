import os
import time
from .elements import WebElement
from .base import BasePage


class AuthPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "http://petfriends1.herokuapp.com/login"
        driver.get(url)
        email = WebElement(id='email')
        passw = WebElement(id='pass')
        btn = WebElement(id='btn-success')
        time.sleep(3)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_pass(self, value):
        self.passw.send_keys(value)

    def btn_click(self):
        self.btn.click()
