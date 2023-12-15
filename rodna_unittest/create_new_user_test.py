import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

new_user = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/ul/li[2]/a')
new_name = (By.CSS_SELECTOR, '#nume_reg')
new_first_name = (By.CSS_SELECTOR, '#prenume_reg')
new_phone = (By.CSS_SELECTOR, '#mobile_reg')
new_country = (By.XPATH, "//select[@id='tara']")
new_email = (By.CSS_SELECTOR, '#email_reg')
new_password = (By.CSS_SELECTOR, '#user_password')
new_register = (By.CSS_SELECTOR, '.btn.btn-success.doRegister')
new_failed_error = (By.ID, 'id="failed_message"')

class NewUserLogin(unittest.TestCase):
    def test_new_user(self):
        expected_result = new_failed_error
        actual_error = expected_result
        self.assertEqual(actual_error, new_failed_error)

driver_00 = webdriver.Chrome()
driver_00.get('https://www.rodnarentacar.ro/')
driver_00.maximize_window()
print(f'New user')

driver_00.find_element(*new_user).click()
time.sleep(1)
driver_00.find_element(*new_name).send_keys('petrica')
time.sleep(1)
driver_00.find_element(*new_first_name).send_keys('moromete')
time.sleep(1)
driver_00.find_element(*new_phone).send_keys('0755000000')
time.sleep(1)
driver_00.find_element(*new_email).send_keys('petrica.moromete@yahoo.com')
driver_00.find_element(*new_password).send_keys('asdf12345')
driver_00.find_element(*new_register).click()
time.sleep(1)

print(f'Start test valid user')
print(f'Create new account')
time.sleep(1)

