import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver, timeout = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout, poll_frequency = 1)

    def _attache_screenshot_on_failer(self, step_name):
        try:
            screenshot = self.driver.get_screenshot_as_png()
            allure.attach(
                screenshot, 
                name = f'screenshot после падения теста: {step_name}', 
                attachment_type = allure.attachment_type.PNG
            )

        except Exception as e:
            print(f'screenshot с ошибкой {e} прикреплен к отчету')

    @allure.step('Найти элемент по локатору {locator}')
    def find_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        
        except Exception:
            self._attache_screenshot_on_failer('find_element')
            raise
    
    @allure.step('Найти видимый элемент по локатору {locator}')
    def find_visible_element(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        
        except Exception:
            self._attache_screenshot_on_failer('find_visible_element')
            raise
    
    @allure.step('Найти список элементов по локатору {locator}')
    def find_elements(self, locator):
        try:
            return self.wait.until(EC.presence_of_elements_located(locator))
        
        except Exception:
            self._attache_screenshot_on_failer('find_elements')
            raise
    
    @allure.step('Клик по элементу {locator}')
    def click(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        
        except Exception:
            self._attache_screenshot_on_failer('click')
            raise
    
    @allure.step('Ввод текста "{text}" в поле {locator}')
    def send_keys(self, locator, text):
        try:
           element = self.find_visible_element(locator)
           element.clear()
           element.send_keys(text)

        except Exception:
            self._attache_screenshot_on_failer('send_keys')
            raise
    
    @allure.step('Получить текст элемента {locator}')
    def get_text(self, locator):
        try:
            return self.find_visible_element(locator).text
        
        except Exception:
            self._attache_screenshot_on_failer('get_text')
            raise
    
    @allure.step('Проверить видимость элемента {locator}')
    def is_element_visible(self, locator):
        try:
            self.find_visible_element(locator)
            return True
        
        except TimeoutException:
            return False

        except Exception:
            self._attache_screenshot_on_failer('is_element_visible')
            raise

    @allure.step('Скролл до элемента {locator}')
    def scroll_to_element(self, locator):
        try:
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        except Exception:
            self._attache_screenshot_on_failer('scroll_to_element')
            raise
        