from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "registration_link")

class LoginPageLocators():
    login_url = (By.ID, "login_link")
    login_form = (By.ID, "login_form")
    register_form = (By.ID, "register_form")
