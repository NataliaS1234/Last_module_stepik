from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, f"'login' substring not found in current URL: {current_url}"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), "Login form is not present"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.register_form), "Register form is not present"
        assert True

    def register_new_user(self,email, password):
        input_email = self.browser.find_element(*LoginPageLocators.email_input)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.password_input)
        input_password.send_keys(password)
        repeat_password = self.browser.find_element(*LoginPageLocators.password_repeat)
        repeat_password.send_keys(password)
        time.sleep(3)
        button = self.browser.find_element(*LoginPageLocators.submit_button)
        button.click()



