import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_phone_details():
    driver = webdriver.Chrome()
    driver.get('https://www.rodnarentacar.ro/')
    time.sleep(2)

    phone_contact = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/ul/li[3]/a')
    phone_contact = driver.find_element(*phone_contact).text

    print(f'Rodna rent-a-car / {phone_contact}')