from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    basket_button = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    info_message = (By.TAG_NAME, "p")


class LoginPageLocators():
    login_url = (By.ID, "login_link")
    login_form = (By.ID, "login_form")
    register_form = (By.ID, "register_form")
    email_input = (By.ID, "id_registration-email")
    password_input = (By.ID, "id_registration-password1")
    password_repeat = (By.ID, "id_registration-password2")
    submit_button = (By.NAME, "registration_submit")


class ProductPageLocators():
    add_to_basket_button = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    success_message = (By.CSS_SELECTOR, ".alertinner strong")
    basket_price = (By.CSS_SELECTOR, ".alertinner p")


class BasePageLocators():
    login_link = (By.ID, "login_link")
    login_link_invalid = (By.CSS_SELECTOR, "#login_link_inc")
    basket_button = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    info_message = (By.TAG_NAME, "p")
    user_icon = (By.XPATH, '// *[ @ id = "messages"] / div / div / i')


