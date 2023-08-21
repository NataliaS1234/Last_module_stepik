from .pages.product_page import ProductPage
import pytest
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
#@pytest.mark.new
#pytest -s -m "new" test_product_page.py


#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


# def test_guest_can_add_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.user_can_click_the_button()
#     #page.should_be_success_message("The shellcoder's handbook")
#     page.should_be_success_message("Coders at Work")
#     page.should_be_basket_total_message("£19.99")


# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.user_can_click_the_button()
#     page.should_not_be_success_message()
#
#
# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.user_can_click_the_button()
#     page.is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.open_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.should_be_empty("Your basket is empty. Continue shopping")


@pytest.mark.new
def test_guest_should_not_see_empty_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = BasketPage(browser, link)
    page.open()
    page.should_not_see_empty_basket("Your basket is empty. Continue shopping")


