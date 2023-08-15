import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Specify the language for the test page")
    parser.addoption("--browser_name", action="store", default="chrome", help="Specify the browser for the test page")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("--language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})
    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", language)
    browser = None
    if browser_name == "chrome":
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        browser = webdriver.Firefox(options=options_firefox)
    yield browser
    browser.quit()





