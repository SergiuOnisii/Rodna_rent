"""
Definim constructor si metodele ce urmeaza sa le utilizam: enter text, get text, etc

"""


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.rodnarentacar.ro/")

    def click(self, by_locator):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator, text):
        assert isinstance(text, object)
        return WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(by_locator)).text


