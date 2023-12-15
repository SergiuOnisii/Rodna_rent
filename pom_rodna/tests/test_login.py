"""
Testam logarea in contul website-ului folosind multiple scenarii
"""
from pom_rodna.pages.login_page import LoginPage
from pom_rodna.pages.menu_page import MenuPage
from pom_rodna.resources.login_locators import LoginLocators
from pom_rodna.tests.base_test import BaseTest


class TestLogin(LoginPage):
    def setUp(self) -> None:
        super().setUp()
        self.menu = MenuPage(self.driver)
        self.login = LoginPage(self.driver)

    def test_valid_email_and_password(self):
        self.menu.click_on_login_user()
        self.login.enter_email('bordura.dumitru@yahoo.com')
        self.login.enter_password('Dumitru')
        self.login.clik_on_login()

    def test_empty_email_and_password(self):
        self.menu.click_on_login_user()
        self.login.clik_on_login()

    def test_wrong_email_and_valid_password(self):
        self.menu.click_on_login_user()
        self.login.enter_email('dumitru@yahoo.com')
        self.login.enter_password('Dumitru')
        self.login.clik_on_login()

    def test_vali_email_and_wrong_password(self):
        self.menu.click_on_login_user()
        self.login.enter_email('bordura.dumitru@yahoo.com')
        self.login.enter_password('0010102')
        self.login.clik_on_login()
