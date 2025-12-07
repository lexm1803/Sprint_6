import pytest
import allure
from data.order_data import ORDER_TEST_DATA
import time

@allure.feature('Страница оформления заказа')
@allure.story('(+)Функционал оформления заказа')
@allure.severity(allure.severity_level.CRITICAL)
class TestOrderScooter:

    @allure.title('Проверка оформления заказа')
    @pytest.mark.parametrize(
            'entry_point',
            ['button_in_header', 'button_in_page'],
            ids=['via_button_in_header', 'via_button_in_page']
    )
    @pytest.mark.parametrize(
        'name, surname, address, metro, phone, date, rental, color, comment',
        ORDER_TEST_DATA,
        ids=['user_1','user_2']
    )
    def test_order_scooter_fill(self, pages, 
                                entry_point, 
                                name, surname, address, metro, phone, 
                                date, rental, color, comment
                                ):
        main = pages['main']
        order = pages['order']
        track = pages['track']
        
        with allure.step('Открываю главную страницу'):
            main.open()
            assert main.is_loaded(), 'Главная страница не загружена'
        
        with allure.step('Нажимаю на кнопку оформления заказа'):
            if entry_point == 'button_in_header':
                main.click_order_button_top()
            else:
                main.click_order_button_in_pages()

            assert order.is_first_form_loaded(), 'Первая форма заказа не загружена'
        
        with allure.step('Заполняю первую форму оформления заказа'):
            order.fill_name(name)
            order.fill_surname(surname)
            order.fill_address(address)
            order.select_metro_station(metro)
            order.fill_phone(phone)
        
        with allure.step('Перехожу на вторую форму оформления'):
            order.click_next()

            assert order.is_second_form_loaded(), 'Вторая форма заказа не загружена'

        with allure.step('Заполняю вторую форму оформления заказа'):
            order.select_date(date)
            order.select_rental(rental)
            order.select_scooter_color(color)
            order.fill_comment(comment)
        
        with allure.step('Нажимаю кнопку оформления заказа'):
            order.click_order_button()

            assert order.is_confirmation_modal_visible(), 'Модальное окно подтверждения заказа не отображено'

        with allure.step('Подтверждаю оформление заказа'):
            order.confirm_order()

            assert order.is_success_modal_visible(), 'Модальное окно успешного заказа не отображено'

        with allure.step('Получаю номер заказа'):
            order_number = order.get_order_number()

            assert order_number.isdigit(), f'Некорректный номер {order_number}'

        with allure.step('Нажимаю на кнопку просмотра заказа'):
            order.click_see_status()

        with allure.step('Проверяю информацию в заказе'):
            assert track.is_order_info_visible(), 'Информация о заказе не отображена'
            assert track.get_order_name() == name, f'Имя в заказе не совпадает с {name}'
            assert track.get_order_surname() == surname, f'Фамилия в заказе не совпадает с {surname}'
            assert track.get_order_address() == address , f'Адрес в заказе не совпадает с {address}'
            assert track.get_order_phone() == phone, f'Телефон в заказе не совпадает с {phone}'
        
        with allure.step('Проверяю работу перехода на главную страницу через логотип'):
            track.click_logo_scooter()
            assert main.driver.current_url == main.URL, f'Адрес страницы не совпадает с {main.URL}'
            assert main.is_loaded(), 'Главная страница не загружена'

        with allure.step('Проверяю работу перехода на Дзен через логотип Яндекса'):
            track.click_logo_yandex()
            assert 'dzen.ru' in main.driver.current_url.lower(), 'Вместо dzen.ru открыт {main.driver.current_url}'
