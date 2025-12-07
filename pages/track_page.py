import allure
import re
from selenium.webdriver.common.by import By
from .main_page import MainPage
from .base_page import BasePage


class TrackPage(BasePage):

    TRACK_INPUT = (By.XPATH, "//input[@class='Input_Input__1iN_Z Track_Input__1g7lq']")
    TRACK_BUTTON = (By.XPATH, "//button[text()='Посмотреть']")

    NOT_FOUND_IMAGE = (By.XPATH, "//div[@class='Track_NotFound__6oaoY']")

    ORDER_INFO_BLOCK = (By.XPATH, "//div[@class='Track_OrderInfo__2fpDL']")
    ORDER_NAME = (By.XPATH, "//div[@class='Track_Title__1XfhB' and text()='Имя']/following-sibling::div[@class='Track_Value__15eEX']")
    ORDER_SURNAME = (By.XPATH, "//div[@class='Track_Title__1XfhB' and text()='Фамилия']/following-sibling::div[@class='Track_Value__15eEX']")
    ORDER_ADDRESS = (By.XPATH, "//div[@class='Track_Title__1XfhB' and text()='Адрес']/following-sibling::div[@class='Track_Value__15eEX']")
    ORDER_METRO = (By.XPATH, "//div[@class='Track_Title__1XfhB' and text()='Станция метро']/following-sibling::div[@class='Track_Value__15eEX']")
    ORDER_PHONE = (By.XPATH, "//div[@class='Track_Title__1XfhB' and text()='Телефон']/following-sibling::div[@class='Track_Value__15eEX']")
    ORDER_DELIVERY_DATE = (By.XPATH, "//div[@class='Track_Title__1XfhB' and text()='Дата доставки']/following-sibling::div[@class='Track_Value__15eEX']")
    ORDER_RENTAL = (By.XPATH, "//div[@class='Track_Title__1XfhB' and text()='Срок аренды']/following-sibling::div[@class='Track_Value__15eEX']")
    ORDER_COLOR = (By.XPATH, "//div[@class='Track_Title__1XfhB' and text()='Цвет']/following-sibling::div[@class='Track_Value__15eEX']")
    ORDER_COMMENT = (By.XPATH, "//div[@class='Track_Title__1XfhB' and text()='Комментарий']/following-sibling::div[@class='Track_Value__15eEX']")

    CANCEL_ORDER_BUTTON = (By.XPATH, "//button[text()='Отменить заказ']")

    STATUS_SCOOTER_AT_WAREHOUSE = (By.XPATH, "//div[contains(@class, 'Track_OrderBrick') and contains(., 'Самокат на складе')]")
    STATUS_COURIER_DELAY = (By.XPATH, "//div[contains(@class, 'Track_OrderBrick') and contains(., 'Курьер задерживается')]")

    CANCEL_MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Хотите отменить заказ?')]")
    CANCEL_MODAL_BUTTON_BACK = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text()='Назад']")
    CANCEL_MODAL_BUTTON_CONFIRM = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text()='Отменить']")

    CANCEL_SUCCESS_MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ отменён')]")
    CANCEL_SUCCESS_BUTTON_OK = (By.XPATH, "//button[text()='Хорошо']")

    URL = 'https://qa-scooter.praktikum-services.ru/track'

    @allure.step('Открыть страницу отслеживания заказа')
    def open(self):
        self.driver.get(self.URL)

    @allure.step('Открыть страницу заказа')
    def open_track_id(self, track_id):
        self.driver.get(f'{self.URL}?t={track_id}')

    @allure.step('Проверить отображение поля ввода номера заказа')
    def is_loaded(self):
        return self.is_element_visible(self.TRACK_INPUT)
    
    @allure.step('Ввести номер заказа {track_id} в поле ввода')
    def enter_track_id(self, track_id):
        self.send_keys(self.TRACK_INPUT, track_id)

    @allure.step('Нажать кнопку "Посмотреть"')
    def click_track_buton(self):
        self.click(self.TRACK_BUTTON)

    @allure.step('Проверить, что заказ не найден')
    def is_order_not_found(self):
        return self.is_element_visible(self.NOT_FOUND_IMAGE)
    
    @allure.step('Проверить отображение блока с информацией о заказе')
    def is_order_info_visible(self):
        return self.is_element_visible(self.ORDER_INFO_BLOCK)
    
    @allure.step('Получить имя из заказа')
    def get_order_name(self):
        return self.get_text(self.ORDER_NAME)
    
    @allure.step('Получить фамилию из заказа')
    def get_order_surname(self):
        return self.get_text(self.ORDER_SURNAME)
    
    @allure.step('Получить адресс из заказа')
    def get_order_address(self):
        return self.get_text(self.ORDER_ADDRESS)
    
    @allure.step('Получить станцию метро из заказа')
    def get_order_metro(self):
        text = self.get_text(self.ORDER_METRO)
        return re.sub(
            r'^[^а-яА-ЯёЁa-zA-Z]+', '', text
        ).strip()
    
    @allure.step('Получить телефон из заказа')
    def get_order_phone(self):
        return self.get_text(self.ORDER_PHONE)
    
    @allure.step('Получить дату доставки заказа')
    def get_order_date(self):
        return self.get_text(self.ORDER_DELIVERY_DATE)
    
    @allure.step('Получить срок аренды из заказа')
    def get_order_rental(self):
        return self.get_text(self.ORDER_RENTAL)
    
    @allure.step('Получить цвет из заказа')
    def get_order_color(self):
        return self.get_text(self.ORDER_COLOR)
    
    @allure.step('Получить комментарий из заказа')
    def get_order_comment(self):
        return self.get_text(self.ORDER_COMMENT)
    
    @allure.step('Проверить отображение статуса "Самокат на складе"')
    def is_scooter_at_warehouse(self):
        return self.is_element_visible(self.STATUS_SCOOTER_AT_WAREHOUSE)
    
    @allure.step('Проверить отображение статуса "Курьер задерживается"')
    def is_scooter_at_delayed(self):
        return self.is_element_visible(self.STATUS_COURIER_DELAY)
    
    @allure.step('Нажать кнопку "Отменить заказ"')
    def click_cancel_order(self):
        self.click(self.CANCEL_ORDER_BUTTON)

    @allure.step('Проверить отображение модального окна отмены заказа')
    def is_cancel_modal_visible(self):
        return self.is_element_visible(self.CANCEL_MODAL_TITLE)
    
    @allure.step('Нажать кнопку "Назад" в модальном окне отмены заказа')
    def click_back(self):
        self.click(self.CANCEL_MODAL_BUTTON_BACK)

    @allure.step('Нажать кнопку "Отменить" в модальном окне отмены заказа')
    def click_cancel_order(self):
        self.click(self.CANCEL_MODAL_BUTTON_CONFIRM)

    @allure.step('Проверить отображение модального окна подтверждения отмены заказа')
    def is_cancel_secces_modal_visible(self):
        return self.is_element_visible(self.CANCEL_SUCCESS_MODAL_TITLE)
    
    @allure.step('Нажать кнопку "Хорошо" в модальном окне успешной отмены заказа')
    def click_cancel_succes_ok(self):
        self.click(self.CANCEL_SUCCESS_BUTTON_OK)

    @allure.step('Нажать на логотип "Самокат"')
    def click_logo_scooter(self):
        self.click(MainPage.LOGO_SCOOTER)

    @allure.step('Нажать на логотип Яндекса')
    def click_logo_yandex(self):
        self.click(MainPage.LOGO_YANDEX)
        self.wait.until(
            lambda d: len(d.window_handles)>1, 
            message = 'Новая вкладка не открыта'
            )
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(
            lambda d: 'dzen.ru' in d.current_url.lower(),
            message = f'Вместо dzen.ru открыт {self.driver.current_url}'
            )
    