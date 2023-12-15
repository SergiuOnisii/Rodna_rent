"""
In acest fisier adaugam meniul principal al site-ului
"""
from pom_rodna.pages.base_page import BasePage
from pom_rodna.resources.menu_locators import MenuLocators, MainMenu, Blog, TermsAndConditions, Contact, Login


class MenuPage(BasePage):
    def __init__(self, driver: object) -> None:
        super().__init__(driver)

    def click_on_prices(self):
        self.click(MenuLocators.price_info)

    def click_on_cars(self):
        self.click(MainMenu.cars_menu)

    def click_on_blog_menu(self):
        self.click(Blog.blog_menu)

    def click_on_t_and_c(self):
        self.click(TermsAndConditions.t_and_c)

    def click_on_contact_menu(self):
        self.click(Contact.contact_menu)


    def click_on_login_user(self):
        self.click(Login.login_user)

    def click_on_new_user(self):
        self.click(Login.new_user)

