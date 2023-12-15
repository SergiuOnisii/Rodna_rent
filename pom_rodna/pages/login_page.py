from pom_rodna.pages.base_page import BasePage
from pom_rodna.resources.login_locators import LoginLocators
import json


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, text):
        self.enter_text(LoginLocators.email_field, text)

    def enter_password(self, text):
        self.enter_text(LoginLocators.password_field, text)

    def clik_on_login(self):
        self.click(LoginLocators.login_btn)

    def setUp(self):
        pass
