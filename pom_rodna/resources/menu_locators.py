from selenium.webdriver.common.by import By


class MenuLocators:
    price_info = (By.ID, '#navbarSupportedContent > ul > li:nth-child(2) > a')
    pick_up_menu = (By.CSS_SELECTOR, '#from_city')
    return_menu = (By.CSS_SELECTOR, '#toCity')


class MainMenu:
    main_menu = (By.ID, '#navbarSupportedContent > ul > li:nth-child(1) > a')
    cars_menu = (By.ID, '#navbarSupportedContent > ul > li:nth-child(3) > a')


class Blog:
    blog_menu = (By.ID, '#navbarSupportedContent > ul > li:nth-child(4) > a')


class TermsAndConditions:
    t_and_c = (By.ID, '#navbarSupportedContent > ul > li:nth-child(5) > a')


class Contact:
    contact_menu = (By.ID, '#navbarSupportedContent > ul > li:nth-child(6) > a')


class Login:
    login_user = (By.ID, '#navbarSupportedContent > ul > li.nav-item.d-block.d-sm-none > a:nth-child(2)')
    new_user = (By.ID, '#navbarSupportedContent > ul > li.nav-item.d-block.d-sm-none > a:nth-child(3)')
