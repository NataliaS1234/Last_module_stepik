from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url):#добавим конструктор — метод, который вызывается, когда мы создаем объект . Конструктор объявляется ключевым словом __init__
        self.browser = browser
        self.url = url

    def open(self):
       self.browser.get(self.url)

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def go_to_the_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.login_link)
        login_link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.login_link), "Login link is not presented"

    def should_be_basket_button(self):
        button = self.browser.find_element(*BasePageLocators.basket_button)
        time.sleep(3)
        button.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.user_icon), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_authorized_user(self):
        pass