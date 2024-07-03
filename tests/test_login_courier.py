import pytest
import requests
import allure
from data import Data


class TestCourierLogin:

    @allure.title('Проверка успешной авторизации')
    @allure.description('Создаем курьера, авторизуемся по логину/паролю, проверяем, что код ответа == 201,\
                        текст ответа содержит id курьера')
    def test_authorization_succsess(self, register_new_courier_and_delete_after_test):
        requests.post(f'{Data.main_page_url}{Data.api_create_courier}', data=register_new_courier_and_delete_after_test)
        del register_new_courier_and_delete_after_test['firstName']
        response = requests.post(f'{Data.main_page_url}{Data.api_login_courier}',
                                 data=register_new_courier_and_delete_after_test)
        assert 200 == response.status_code and 'id' in response.text, \
            (f'Ожидаемый код: 201, полученный код: {response.status_code}, \
             ожидаемый текст содержит: "id", полученный текст: {response.text}')

    @allure.title('Проверка запрета авторизации курьера с пустым полем логин или пароль')
    @allure.description('Создаем курьера, при заполнении формы авторизации поле логин или пароль оставляем пустым, проверяем что \
            код ответа == 400, текст ответа: "Недостаточно данных для входа"')
    @pytest.mark.parametrize('missing_argument', (('login'), ('password')))
    def test_login_courier_without_login_or_password(self, register_courier_profile, missing_argument):
        requests.post(f'{Data.main_page_url}{Data.api_create_courier}', data=register_courier_profile)
        del register_courier_profile[missing_argument]
        response = requests.post(f'{Data.main_page_url}{Data.api_login_courier}', data=register_courier_profile)
        assert 400 == response.status_code and Data.text_login_400 in response.text, \
        f'Ожидаемый код: 400, полученный код: {response.status_code}, ожидаемый текст содержит: \
        {Data.text_login_400}, полученный текст: {response.text}'
#Тест не проходит при пустом поле пароль из-за некорректного кода ответа от сервера - 504 вместо ожидаемого 400
#Текст ответа отличается: ожидаемый Недостаточно данных для входа, полученный текст: Service unavailable

    @allure.title('Проверка запрета авторизации при заполнении поля логин или пароль некорректным значением')
    @allure.description('Создаем курьера, в форме авторизации заполняем поле логин или пароль некорректным значением, \
                        проверяем что код ответа == 404, текст ответа: "Учетная запись не найдена"')
    @pytest.mark.parametrize('incorrect_argument', (('login'), ('password')))
    def test_login_courier_with_invalid_login_or_password(self, register_courier_profile, incorrect_argument):
        requests.post(f'{Data.main_page_url}{Data.api_create_courier}', data=register_courier_profile)
        register_courier_profile[incorrect_argument] = 'error'
        response = requests.post(f'{Data.main_page_url}{Data.api_login_courier}', data=register_courier_profile)
        r = response.json()
        assert 404 == r['code'] and Data.text_login_404 == r['message'], (f'Ожидаемый код: 404, \
        полученный код: {r['code']}, ожидаемый текст: {Data.text_login_404}, полученный текст: {r['message']}')
