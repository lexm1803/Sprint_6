import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.track_pages import TrackPage


@pytest.fixture(scope='session')
def driver():
    options = Options()
    options.add_argument('--headless')

    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(0)

    driver.get('https://qa-scooter.praktikum-services.ru/')
    try:
        button = driver.find_element('id', 'rcc_confirm_button')
        button.click()
        driver.implicitly_wait(1)
    except Exception:
        pass

    yield driver

    driver.quit()

@pytest.fixture
def pages(driver):
    return {
        "main": MainPage(driver),
        "order": OrderPage(driver),
        "track": TrackPage(driver)
    }
