"""
Vrem sa testam sectiune de alege autoturism, preluare din oras Cluj in data de 25 decembrie ora 10.00am si
returnare in data de 27 decembrie ora 14.00pm, la aeroport. Ne dorim un BMW Seria 3

"""
import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

pick_up_place = (By.ID, 'from_city')
pick_up_city = (By.CSS_SELECTOR, '#from_city > option:nth-child(2)')
pick_up_airport = (By.CSS_SELECTOR, '#from_city > option:nth-child(1)')

return_place = (By.CSS_SELECTOR, '#toCity')
return_city = (By.CSS_SELECTOR, '#toCity > option:nth-child(2)')
return_airport = (By.CSS_SELECTOR, '#toCity > option:nth-child(1)')

pick_up_date = (By.CSS_SELECTOR, '#date1')
pick_up_25december = (By.CSS_SELECTOR, '#ui-datepicker-div > table > tbody > tr:nth-child(5) > td:nth-child(2) > a')
pick_up_hour = (By.ID, 'pick-up-time')

pick_up_10am = (By.XPATH, '//*[@id="pick-up-time"]/option[19]')
pop_up = (By.CSS_SELECTOR, '#euCookieAccept')
return_date = (By.CSS_SELECTOR, '#date2')
return_27december = (By.CSS_SELECTOR, '#ui-datepicker-div > table > tbody > tr:nth-child(5) > td:nth-child(4) > a')
return_14hour = (By.CSS_SELECTOR, '#drop-off-time > option:nth-child(27)')
pick_vehicle = (By.CSS_SELECTOR, '#frm-rez')
bmw_seria3 = (By.CSS_SELECTOR, '#car-body-53')
bmw_select = (By.XPATH, '//*[@id="53"]')
expected_vehicle = bmw_seria3

class SearchVehicle(unittest.TestCase):
    def test_search_bmw(self):
        expected_result = expected_vehicle
        actual_error = expected_result
        self.assertEqual(actual_error, expected_vehicle)


driver_00 = webdriver.Chrome()
driver_00.get('https://www.rodnarentacar.ro/')
driver_00.maximize_window()
print(f'Select vehicle for Christmas day')
driver_00.find_element(*pick_up_place).click()
driver_00.find_element(*pick_up_city).click()
time.sleep(2)
driver_00.find_element(*return_place).click()
driver_00.find_element(*return_airport).click()
time.sleep(2)
driver_00.find_element(*pick_up_date).click()
driver_00.find_element(*pick_up_25december).click()
time.sleep(2)
driver_00.find_element(*pick_up_hour).click()
driver_00.find_element(*pick_up_10am).click()
time.sleep(2)
driver_00.find_element(*pop_up).click()
time.sleep(2)
driver_00.find_element(*return_date).click()
driver_00.find_element(*return_27december).click()
driver_00.find_element(*return_14hour).click()
time.sleep(2)
driver_00.find_element(*pick_vehicle).click()
time.sleep(2)
actions = ActionChains(driver_00)
actions.send_keys(Keys.PAGE_DOWN)
actions.perform()
bmw_seria3 = driver_00.find_element(*bmw_seria3)
driver_00.find_element(*bmw_select).click()
time.sleep(2)
print(f'Nice job')
