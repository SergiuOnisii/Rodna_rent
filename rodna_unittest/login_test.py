import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

login_user = (By.XPATH, "//a[@class='ac'][contains(text(),'Intră în cont')]")
email_field = (By.CSS_SELECTOR, '#email')
password_field = (By.CSS_SELECTOR, '#password')
login_btn = (By.XPATH, "//button[contains(text(),'Intră în cont')]")
error_login = (By.CSS_SELECTOR, '.alert.alert-danger.mt-5.mb-5')
expected_error = error_login
actual_error = 'Date de logare greşite. Vă rugam incercaţi din nou.'
expected_user = 'bordura.dumitru@yahoo.com'
expected_password = 'Dumitru'
user_menu = (By.ID, 'dropdownMenuButton')
log_out_button = (By.CSS_SELECTOR,
                  'body > div.multi > div.container.toph.nopadding.d-none.d-sm-block.d-md-block.d-lg-block > div.col-md-12.text-right > div > div > a:nth-child(5)')

driver_00 = webdriver.Chrome()
driver_00.get('https://www.rodnarentacar.ro/')
driver_00.maximize_window()
print(f'Start test invalid user')

time.sleep(1)
driver_00.find_element(*login_user).click()
time.sleep(1)
driver_00.find_element(*email_field).send_keys('nume@yahoo.com')
driver_00.find_element(*password_field).send_keys('12023')
driver_00.find_element(*login_btn).click()
time.sleep(1)


class UserLogin(unittest.TestCase):
    def test_user_invalid(self):
        expected_result = expected_error
        actual_error = expected_result
        self.assertEqual(actual_error, expected_error)


print(f'Valid Login')
time.sleep(1)
driver_00.find_element(*login_user).click()
time.sleep(2)
driver_00.find_element(*email_field).send_keys('bordura.dumitru@yahoo.com')
driver_00.find_element(*password_field).send_keys('Dumitru')
driver_00.find_element(*login_btn).click()
time.sleep(2)
driver_00.find_element(*user_menu).click()
driver_00.find_element(*log_out_button).click()
time.sleep(2)
