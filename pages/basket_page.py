from .locators import BasePageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_empty(self, expected_message):
        info_message_element = self.browser.find_element(*BasePageLocators.info_message)
        info_message = info_message_element.text
        print(info_message)
        assert self.is_element_present(*BasePageLocators.info_message), "Info message is not present"
        assert info_message in expected_message, f"Expected '{expected_message}' in '{info_message}'"

    def should_not_see_empty_basket(self, expected_message):
        info_message_element = self.browser.find_element(*BasePageLocators.info_message)
        info_message = info_message_element.text
        print(info_message)
        assert self.is_not_element_present(*BasePageLocators.info_message), \
            "Success message is presented, but should not be"
