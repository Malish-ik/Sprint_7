import requests
import allure
from data import Data

class TestListOfOrders:
    @allure.title('Проверка отображения в теле ответа списка заказов')
    @allure.description('Отправляем запрос на возврат списка заказов с лимитом 3 и около станции "Калужская"\
                        проверяем, что вывелось 3 заказа, станция "Калужская"')
    def test_list_of_orders(self):
        response = requests.get(f'{Data.main_page_url}{Data.api_order}?limit=3&page=0&nearestStation=["110"]')
        r = response.json()
        assert len(r['orders']) == 3 and r['availableStations'][0]['name'] == 'Калужская',\
            f'ожидавлось 3 заказа получили {len(r['orders'])}, ожидалось "Калужская", \
            получили {r['availableStations'][0]['name']}'


