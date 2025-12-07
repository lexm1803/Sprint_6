import pytest
from allure import severity, severity_level

@severity(severity_level.CRITICAL)
class TestMainPage:

    def test_main_title_is_visible(self, main_page):
        main_page.open()
        assert main_page.is_loaded(), 'Главная страница не загружена'
        assert main_page.is_visible_main_title(), 'Заголовок на главной странице не отображен'
        assert main_page.is_visible_main_sub_title(), 'Описание на главной странице не отображено'
        assert main_page.is_visible_button_order_on_the_page(), 'Кнопка "Заказать" на странице не отображена'
        assert main_page.is_visible_logo_scooter(), 'Логотип "Самокат" не отображен'
        assert main_page.is_visible_logo_yandex(), 'Логотип "Яндекс" не отображен'
        assert main_page.is_visible_how_it_work_title(), 'Заголовок "Как это работает" не оотображен'
        assert main_page.is_visible_faq_section_title(), 'Заголовок "Вопросы о важном" не отображен'