from.base_page import BasePage
from selenium.webdriver.common.by import By
#/корень текущего диска
# ./текущая директория
# ../родитель текущей директории


class MainPage(BasePage): #класс предок указывается в скобках
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

