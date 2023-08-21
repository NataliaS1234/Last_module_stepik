import time

from.base_page import BasePage
from .locators import MainPageLocators
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#/корень текущего диска
# ./текущая директория
# ../родитель текущей директории
#  хорошей практикой является выносить селектор во внешнюю переменную.


class MainPage(BasePage): #класс предок указывается в скобках
    pass
    # def should_be_basket_button(self):
    #     button = self.browser.find_element(*MainPageLocators.basket_button)
    #     time.sleep(3)
    #     button.click()

    # def should_be_empty(self, expected_message):
    #     info_message_element = self.browser.find_element(*MainPageLocators.info_message)
    #     info_message = info_message_element.text
    #     print(info_message)
    #     assert self.is_element_present(*MainPageLocators.info_message), "Info message is not present"
    #     assert info_message in expected_message, f"Expected '{expected_message}' in '{info_message}'"














