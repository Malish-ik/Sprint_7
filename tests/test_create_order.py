import pytest
import requests
import allure
from data import Data


class TestCreateOrder:

    @allure.title('Проверка создания заказа с разными вариантами цвета самоката')
    @allure.description('Создаем заказ, передаем в параметре color возможные цвета по отдельности, \
    оба цвета сразу, не выбираем ни одного цвета, проверяем, что код ответа == 201, текст ответа содержит track')
    @pytest.mark.parametrize("color", Data.color_data)
    def test_order_any_color_success(self, register_new_order, color):
        register_new_order['color'] = color
        response = requests.post(f'{Data.main_page_url}{Data.api_order}', data=register_new_order, timeout=7)
        assert 201 == response.status_code and 'track' in response.text, \
            (f'Ожидаемый код: 201, полученный код: {response.status_code}, \
             ожидаемый текст содержит: "track", полученный текст: {response.text}')

#Тест не проходит при выборе одного цвета самоката - код ответа 500 вместо ожидаемого 201
#Oжидаемый текст содержит: "track", полученный текст: {"code":500,"message":"values.map is not a function"}
#При выборе двух цветов или ни одного - тест проходит


