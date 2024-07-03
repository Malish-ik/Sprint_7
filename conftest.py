import pytest
import requests
from data import Data

@pytest.fixture()
def register_courier_profile():
    payload = {
        "login": Data.login,
        "password": Data.password,
        "firstName": Data.firstName
    }
    return payload



@pytest.fixture()
def register_new_courier_and_delete_after_test(register_courier_profile):
    yield register_courier_profile
    response = requests.post(f'{Data.main_page_url}/api/v1/courier/login',
                                data={"login": register_courier_profile['login'], "password": register_courier_profile['password']})
    id_courier = response.json()
    requests.delete(f'{Data.main_page_url}/api/v1/courier/{id_courier["id"]}')

@pytest.fixture()
def register_new_order():
    order_data = {
        "firstName": Data.firstName,
        "lastName": Data.lastName,
        "adress": Data.address,
        "metroStation": Data.metroStation,
        "phone": Data.phone,
        "rentTime": Data.rentTime,
        "deliveryDate": Data.deliveryDate,
        "comment": Data.comment
    }
    yield order_data

