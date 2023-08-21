from.base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage

#/корень текущего диска
# ./текущая директория
# ../родитель текущей директории
#  хорошей практикой является выносить селектор во внешнюю переменную.


class MainPage(BasePage): #класс предок указывается в скобках
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
#Как вы уже знаете, метод __init__ вызывается при создании объекта.
# Конструктор выше с ключевым словом super на самом деле только вызывает конструктор класса предка
# и передает ему все те аргументы, которые мы передали в конструктор MainPage.







