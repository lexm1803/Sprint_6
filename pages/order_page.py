import re
import allure
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):

    FORM_TITLE_FIRST = (By.XPATH, "//div[text()='Для кого самокат']")
    FIELD_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    FIELD_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    FIELD_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    FIELD_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    FIELD_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    FORM_TITLE_SECOND = (By.XPATH, "//div[text()='Про аренду']")
    FIELD_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DROPDOWN_RENTAL = (By.XPATH, "//div[@class='Dropdown-control']")
    DROPDOWN_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='{}']")
    CHECKBOX_BLACK = (By.ID, "black")
    CHECKBOX_GREY = (By.ID, "grey")
    FIELD_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_PICKER = (By.CLASS_NAME, 'react-datepicker')
    DATEPICKER_DAY = (
        By.XPATH,
        "//div[contains(@class, 'react-datepicker__day') "
        "and not(contains(@class, 'outside-month')) "
        "and not(contains(@class, 'disabled')) "
        "and text()='{}']"
    )

    MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Хотите оформить заказ?')]")
    MODAL_BUTTON_YES = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text()='Да']")
    MODAL_BUTTON_NO = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text()='Нет']")

    SUCCESS_MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")
    SUCCESS_MODAL_ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Order_Text__2broi') and contains(text(), 'Номер заказа')]")
    SUCCESS_BUTTON_STATUS = (By.XPATH, "//button[text()='Посмотреть статус']")

    URL = 'https://qa-scooter.praktikum-services.ru/order'

    @allure.step('Открыть страницу оформления заказа')
    def open(self):
        self.driver.get(self.URL)

    @allure.step('Проверить, что первая форма загружена')
    def is_first_form_loaded(self):
        return self.is_element_visible(self.FORM_TITLE_FIRST)
    
    @allure.step('Проверить, что вторая форма загружена')
    def is_second_form_loaded(self):
        return self.is_element_visible(self.FORM_TITLE_SECOND)
    
    @allure.step('Ввести значение в поле "Имя": {name}')
    def fill_name(self, name):
        self.send_keys(self.FIELD_NAME, name)

    @allure.step('Ввести значение в поле "Фамилия": {surname}')
    def fill_surname(self, surname):
        self.send_keys(self.FIELD_SURNAME, surname)

    @allure.step('Ввести значение в поле "Адрес": {address}')
    def fill_address(self, address):
        self.send_keys(self.FIELD_ADDRESS, address)

    @allure.step('Выбрать станцию метро: {station}')
    def select_metro_station(self, station):
        metro_input = self.find_visible_element(self.FIELD_METRO)
        metro_input.click()
        metro_input.send_keys(station)
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)

    @allure.step('Заполнить поле "Телефон": {phone}')
    def fill_phone(self, phone):
        self.send_keys(self.FIELD_PHONE, phone)

    @allure.step('Нажать кнопку "Далее"')
    def click_next(self):
        self.click(self.NEXT_BUTTON)

    @allure.step('Выбрать дату: {date}')
    def select_date(self, date):
        self.click(self.DATE_INPUT)
        self.wait.until(EC.presence_of_element_located(self.DATE_PICKER))
        day_locator = (
            self.DATEPICKER_DAY[0],
            self.DATEPICKER_DAY[1].format(date)
        )
        self.wait.until(
            EC.element_to_be_clickable(day_locator),
            message = f'День {date} стал кликабельным'
        )
        self.click(day_locator)

    @allure.step('Выбрать срок аренды: {rental}')
    def select_rental(self, rental):
        self.click(self.DROPDOWN_RENTAL)
        option_locator = (
            self.DROPDOWN_OPTION[0],
            self.DROPDOWN_OPTION[1].format(rental)
        )
        self.click(option_locator)

    @allure.step('Выбрать цвет самоката: {color}')
    def select_scooter_color(self, color):
        if color == 'black':
            self.click(self.CHECKBOX_BLACK)
        elif color == 'gray':
            self.click(self.CHECKBOX_GREY)
        elif color == 'both':
            self.click(self.CHECKBOX_BLACK)
            self.click(self.CHECKBOX_GREY)

    @allure.step('Ввести значение в поле "Комментарий": {comment}')
    def fill_comment(self, comment):
        if comment:
            self.send_keys(self.FIELD_COMMENT, comment)

    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button(self):
        self.click(self.ORDER_BUTTON)

    @allure.step('Проверить, что модальное окно подтверждения отображено')
    def is_confirmation_modal_visible(self):
        return self.is_element_visible(self.MODAL_TITLE)

    @allure.step('Нажать кнопку "Да" в модальном окне подтверждения заказа')
    def confirm_order(self):
        self.click(self.MODAL_BUTTON_YES)

    @allure.step('Нажать кнопку "Нет" в модальном окне подтверждения заказа')
    def cancel_order(self):
        self.click(self.MODAL_BUTTON_NO)

    @allure.step('Проверить, что модальное окно успешного заказа отображено')
    def is_success_modal_visible(self):
        return self.is_element_visible(self.SUCCESS_MODAL_TITLE)
    
    @allure.step('Получить номер заказа')
    def get_order_number(self):
        locator = self.SUCCESS_MODAL_ORDER_NUMBER
        self.wait.until(
            lambda _: re.search(
                r'Номер заказа:\s*\d+', self.get_text(locator)
            ), message = 'Номер заказа не появился в модальном окне'
        )
        text = self.get_text(locator)
        match = re.search(
            r'Номер заказа:\s*(\d+)', text
        )
        if not match:
            raise ValueError(f'Не удалось извлечь номер заказа из текста: {text}')
        return match.group(1)
    
    @allure.step('Нажать на кнопку "Посмотреть статус"')
    def click_see_status(self):
        self.click(self.SUCCESS_BUTTON_STATUS)
        