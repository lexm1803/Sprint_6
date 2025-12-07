import allure
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    MAIN_TITLE = (By.XPATH, '//div[@class="Home_Header__iJKdX"]')
    MAIN_DESCRIPTION = (By.XPATH, '//div[@class="Home_Header__iJKdX"]/div[@class="Home_SubHeader__zwi_E"]')

    BUTTON_ORDER_IN_THE_HEADER = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[text()='Заказать']")
    BUTTON_ORDER_ON_THE_PAGE = (By.XPATH, "//div[contains(@class, 'FinishButton')]//button[text()='Заказать']")

    LOGO_SCOOTER = (By.XPATH, "//a[@href='/']//img[@alt='Scooter']")
    LOGO_YANDEX = (By.XPATH, "//a[@href='//yandex.ru']//img[@alt='Yandex']")

    HOW_IT_WORKS_TITLE = (By.XPATH, "//div[text()='Как это работает']")
    FIRST_STEP_TITLE = (By.XPATH, "//div[text()='Заказываете самокат']")
    FIRST_STEP_DESC = (By.XPATH, "//div[text()='Выбираете, когда и куда привезти']")

    FAQ_SECTION_TITLE = (By.XPATH, "//div[text()='Вопросы о важном']")
    FAQ_CONTAINER = (By.XPATH, "//div[@data-accordion-component='Accordion']")
    FAQ_ITEM = (By.XPATH, ".//div[@data-accordion-component='AccordionItem']")
    FAQ_BUTTON = (By.XPATH, ".//div[@data-accordion-component='AccordionItemButton']")
    FAQ_PANEL = (By.XPATH, ".//div[@data-accordion-component='AccordionItemPanel']")

    COOKIE_BANNER = (By.CLASS_NAME, "App_CookieConsent__1yUIN")
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")

    TRACK_INPUT_HEADER = (By.XPATH, "//input[@placeholder='Введите номер заказа']")
    TRACK_BUTTON_HEADER = (By.XPATH, "//button[text()='Go!']")
    STATUS_BUTTON = (By.XPATH, "//button[text()='Статус заказа']")

    URL = 'https://qa-scooter.praktikum-services.ru/'

    # Перенести в base
    @allure.step('Открыть главную страницу')
    def open(self):
        self.driver.get(self.URL)
        self.accept_cookies_if_present()

    @allure.step('Проверить наличие заголовка на главной странице')
    def is_visible_main_title(self):
        return self.is_element_visible(self.MAIN_TITLE)
    
    @allure.step('Проверить отображение описания под заголовком на главной странице')
    def is_visible_main_sub_title(self):
        return self.is_element_visible(self.MAIN_DESCRIPTION)
    
    @allure.step('Проверить отображение кнопки "Заказать" на странице')
    def is_visible_button_order_on_the_page(self):
        return self.is_element_visible(self.BUTTON_ORDER_ON_THE_PAGE)
    
    @allure.step('Проверить отображение логотипа "Самокат"')
    def is_visible_logo_scooter(self):
        return self.is_element_visible(self.LOGO_SCOOTER)
    
    @allure.step('Проверить отображение логотипа "Яндекс"')
    def is_visible_logo_yandex(self):
        return self.is_element_visible(self.LOGO_YANDEX)
    
    @allure.step('Проверить отображение заголовка "Как это работает"')
    def is_visible_how_it_work_title(self):
        return self.is_element_visible(self.HOW_IT_WORKS_TITLE)
    
    @allure.step('Проверить отображение заголовка "Вопросы о важном"')
    def is_visible_faq_section_title(self):
        return self.is_element_visible(self.FAQ_SECTION_TITLE)

    @allure.step('Принять cookie, если баннер отображен')
    def accept_cookies_if_present(self):
        try:
            if self.is_element_visible(self.COOKIE_BANNER):
                self.click(self.COOKIE_ACCEPT_BUTTON)
                #TO DO: явное ожидание перенести в base?
                self.wait.until(EC.invisibility_of_element_located(self.COOKIE_BANNER))
        except Exception:
            pass
    
    @allure.step('Проверка, что страница загружена')
    def is_loaded(self):
        try:
            return self.is_element_visible(self.MAIN_TITLE)
        except Exception:
            return False

    @allure.step('Клик по кнопке "Заказать" в хэдере')
    def click_order_button_top(self):
        self.click(self.BUTTON_ORDER_IN_THE_HEADER)

    @allure.step('Клик по кнопке "Заказать" на странице')
    def click_order_button_in_pages(self):
        self.scroll_to_element(self.BUTTON_ORDER_ON_THE_PAGE)
        self.click(self.BUTTON_ORDER_ON_THE_PAGE)

    @allure.step('Нажать на логотип самоката')
    def click_logo_scooter(self):
        self.click(self.LOGO_SCOOTER)

    @allure.step('Нажать на логотип Яндекс')
    def click_logo_yandex(self):
        self.click(self.LOGO_YANDEX)

    @allure.step('Получение списка количества вопросов в блоке FAQ')
    def get_faq_count(self):
        conteiner = self.find_element(self.FAQ_CONTAINER)
        items = conteiner.find_elements(*self.FAQ_ITEM)
        return len(items)
    
    @allure.step('Получение текста вопроса №{index}')
    def get_faq_question_text(self, index):
        conteiner = self.find_element(self.FAQ_CONTAINER)
        items = conteiner.find_elements(*self.FAQ_ITEM)
        if index >= len(items):
            raise IndexError(f'Индекс {index} выходит за пределы списка вопросов {len(items)}')
        button = items[index].find_element(*self.FAQ_BUTTON)
        return button.text.strip()
    
    @allure.step('Раскрыть вопрос №{index}')
    def click_faq_question(self, index):
        conteiner = self.find_element(self.FAQ_CONTAINER)
        items = conteiner.find_elements(*self.FAQ_ITEM)
        if index >= len(items):
            raise IndexError(f'Индекс {index} выходит за пределы списка вопросов {len(items)}')
        button = items[index].find_element(*self.FAQ_BUTTON)
        # TO DO: создать метод вставки JS в консоль в base?
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        self.driver.execute_script(
            "arguments[0].style.zIndex = '9999'; "
            "arguments[0].style.position = 'relative';",
            button
        )
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step('Получить текст ответа на вопрос №{index}')
    def get_faq_answer_text(self, index):
        conteiner = self.find_element(self.FAQ_CONTAINER)
        items = conteiner.find_elements(*self.FAQ_ITEM)
        if index >= len(items):
            raise IndexError(f'Индекс {index} выходит за пределы списка вопросов {len(items)}')
        panel = items[index].find_element(*self.FAQ_PANEL)
        #TO DO: подумать над другой реализацией
        self.wait.until(
            lambda driver: panel.text.strip() != '', 
            message = f'Ответ №{index} пуст'
        )
        return panel.text.strip()
    
    #TO DO: перенести в base?
    @allure.step('Ввести номер заказа в хэдере: {track_id}')
    def enter_track_id_in_header(self, track_id):
        self.send_keys(self.TRACK_INPUT_HEADER, track_id)

    @allure.step('Нажать на "Go" в хэдере')
    def click_track_go_button(self):
        self.click(self.TRACK_BUTTON_HEADER)

    @allure.step('Нажать на кнопку "Статус заказа"')
    def click_status_button(self):
        self.click(self.STATUS_BUTTON)
    