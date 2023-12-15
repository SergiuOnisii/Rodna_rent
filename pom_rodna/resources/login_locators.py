from selenium.webdriver.common.by import By

class LoginLocators:
    email_field = (By.CSS_SELECTOR, '#email')
    password_field = (By.CSS_SELECTOR, '#password')
    login_user = (By.XPATH,"//a[@class='ac'][contains(text(),'Intră în cont')]")
    

