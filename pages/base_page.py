
class BasePage():
    def __init__(self, browser, url):#добавим конструктор — метод, который вызывается, когда мы создаем объект . Конструктор объявляется ключевым словом __init__
        self.browser = browser
        self.url = url

    def open(self):
       self.browser.get(self.url)