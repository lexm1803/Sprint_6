import pytest
from allure import severity, severity_level
from data.order_data import FAQ_DATA

@severity(severity_level.NORMAL)
class TestFAQDropdown:

    @pytest.mark.parametrize(
            "index, questions, expected_answer", 
            [(i,q,a) for i, (q,a) in enumerate(FAQ_DATA)],
            ids=[f'faq_{i+1}: {q[:20]}' for i,(q,_) in enumerate(FAQ_DATA)]
    )
    def test_faq_question_correctly(self, main_page, index, questions, expected_answer):
        main_page.open()
        assert main_page.is_loaded()

        actual_question = main_page.get_faq_question_text(index)
        assert actual_question == questions, f'Вопрос {index} не совпадает'

        main_page.click_faq_question(index)
        
        actual_answer = main_page.get_faq_answer_text(index)
        assert expected_answer in actual_answer, f'Ответ {index} не содержит ожидаемый текст'
        