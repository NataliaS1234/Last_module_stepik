import time

from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def user_can_click_the_button(self):
        button = self.browser.find_element(*ProductPageLocators.add_to_basket_button)
        button.click()
        self.solve_quiz_and_get_code()
        time.sleep(5)

    def should_be_success_message(self, book_title):
        #assert self.is_element_present(*ProductPageLocators.success_message), "success message is not correct"
        success_message = self.browser.find_element(*ProductPageLocators.success_message).text
        assert book_title in success_message, f"Expected '{book_title}' in '{success_message}'"

    def should_be_basket_total_message(self, price):
        basket_price = self.browser.find_element(*ProductPageLocators.basket_price).text
        assert price in basket_price, f"Expected '{price}' in {basket_price}"
        #Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
#Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.


