# Здесь и далее мы будем использовать эту команду для запуска.
# В этой команде мы использовали опцию PyTest --tb=line, которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста.
# Так вам будет проще разобраться в том, как выглядят сообщения об ошибках.
#/корень текущего диска
# ./текущая директория
# ../родитель текущей директории

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com"  #for this link id = login_link
#     page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
#     page.open()  # открываем страницу
#     page.go_to_the_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()
#
#
# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.should_be_empty("Your basket is empty. Continue shopping")


def test_guest_should_not_see_empty_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser, link)
    page.open()
    page.should_not_see_empty_basket("Your basket is empty. Continue shopping")






