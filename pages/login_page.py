from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, f"'login' substring not found in current URL: {current_url}"
        assert True
        #     login_url = self.browser.find_element(*LoginPageLocators.login_url)
        #     href_value = login_url.get_attribute("href")
        #     assert self. is_element_present(*LoginPageLocators.login_url), "Login url is not present"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), "Login form is not present"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.register_form), "Register form is not present"
        assert True


