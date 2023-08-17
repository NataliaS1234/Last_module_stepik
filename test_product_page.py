from .pages.product_page import ProductPage
import pytest


#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.user_can_click_the_button()
    #page.should_be_success_message("The shellcoder's handbook")
    page.should_be_success_message("Coders at Work")
    page.should_be_basket_total_message("£19.99")




