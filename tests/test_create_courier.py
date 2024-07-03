import pytest
import requests
import allure
from data import Data


class TestCreateCourier:

    @allure.title('Успешное создание курьера')
    @allure.description('Создаем курьера, проверяем, что код ответа == 201,\
                        текст ответа: "ok":true')
    def test_create_courier_success(self, register_new_courier_and_delete_after_test):
        response = requests.post(f'{Data.main_page_url}{Data.api_create_courier}', data=register_new_courier_and_delete_after_test)
        assert 201 == response.status_code and Data.text_create_201 == response.text

    @allure.title('Запрет создания курьеров с одинаковыми данными')
    @allure.description('Создаем двух курьеров с одинаковыми данными, \
                        проверяем, что код ответа == 409, текст ответа: "Этот логин уже используется"')
    def test_create_two_couriers_with_the_same_data(self, register_new_courier_and_delete_after_test):
        requests.post(f'{Data.main_page_url}{Data.api_create_courier}', data=register_new_courier_and_delete_after_test)
        response = requests.post(f'{Data.main_page_url}{Data.api_create_courier}', data=register_new_courier_and_delete_after_test)
        r = response.json()
        assert 409 == r['code'] and Data.text_create_409 == r['message'], \
            f'Ожидаемый код: 409, полученный код: {r['code']}, ожидаемый текст: {Data.text_create_409}, \
            полученный текст: {r['message']}'
# Тест не проходит из-за несоответствия текста ответа из документации и текста по факту.
# В документации в тексте "Этот логин уже используется", по факту "Этот логин уже используется. Попробуйте другой."

    @allure.title('Проверка запрета создания курьера с пустым полем Логин или Пароль')
    @allure.description('Создаем курьера без логина или пароля, проверяем что код ответа == 400, \
    текст ответа: "Недостаточно данных для создания учетной записи"')
    @pytest.mark.parametrize('missing_argument', (('login'),('password')))
    def test_create_courier_failed_without_login_or_password(self, register_courier_profile, missing_argument):
        del register_courier_profile[missing_argument]
        response = requests.post(f'{Data.main_page_url}{Data.api_create_courier}', data=register_courier_profile)
        r = response.json()
        assert 400 == r['code'] and Data.text_create_400 == r['message'], \
            f'Ожидаемый код: 400, полученный код: {r['code']}, ожидаемый текст: \
             {Data.text_create_400}, полученный текст: {r["message"]}'

    @allure.title('Проверка успешного создания курьера c пустым полем Имя')
    @allure.description('Создаем курьера, поле Имя оставляем пустым, проверяем, что код ответа == 201,\
                        текст ответа: "ok":true')
    def test_create_courier_success_without_first_name(self, register_courier_profile):
        del register_courier_profile['firstName']
        response = requests.post(f'{Data.main_page_url}{Data.api_create_courier}', data=register_courier_profile)
        assert 201 == response.status_code and Data.text_create_201 == response.text, f'Ожидаемый код: 201, \
        полученный код: {response.status_code}, ожидаемый текст: {Data.text_create_201}, полученный текст: {response.text}'



