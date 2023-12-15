"""
Mostenim clasa BasePage folosind super().__init_ ca keyword pe

"""
from selenium.webdriver.chrome import webdriver

#
# from pom.pages.base_page import BasePage
# from pom.resources.home_locators import HomePageLocators
from pom_rodna.pages.base_page import BasePage
from selenium import webdriver

from pom_rodna.resources.home_locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super ().__init__(driver)
        self.get_textHomePageLocators = None

    def get_phone_contact(self):
        return self.get_textHomePageLocators.phone_contact

    def main_menu(self):
        return self.get_text

    def click_pick_up_menu(self):
        pass

    def click_return_menu(self):
       pass


