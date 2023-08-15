from .base_page import BasePage


class MainPage(BasePage): #класс предок указывается в скобках
    def go_to_login_page(browser):
        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()