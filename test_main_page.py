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


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина