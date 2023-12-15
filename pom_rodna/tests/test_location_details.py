"""
creem un test pentru a verifica detalile locatiei: program de functionare si numar de contact

"""

import unittest
from selenium import webdriver

from pom_rodna.pages.home_page import HomePage
from pom_rodna.tests.base_test import BaseTest


class TestLocationDetails(BaseTest):

    def setUp(self) -> None:
        super().setUp()
        self.home_page = HomePage(self.driver)

    def test_phone_contact(self):
        text = self.home_page.get_phone_contact()
        self.assertIn("+", text)

    def test_main_menu(self):
        text = self.home_page.main_menu()
        return self.assertIn("Meniu principal", text)



if __name__ == '__main__':
    unittest.main()
