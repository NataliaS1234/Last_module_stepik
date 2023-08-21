from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators():
    login_url = (By.ID, "login_link")
    login_form = (By.ID, "login_form")
    register_form = (By.ID, "register_form")


class ProductPageLocators():
    add_to_basket_button = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    success_message = (By.CSS_SELECTOR, ".alertinner strong")
    basket_price = (By.CSS_SELECTOR, ".alertinner p")


class BasePageLocators():
    login_link = (By.ID, "login_link")
    login_link_invalid = (By.CSS_SELECTOR, "#login_link_inc")



