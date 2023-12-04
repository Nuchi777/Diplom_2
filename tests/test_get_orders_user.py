import allure
import requests
from data import Urls, Endpoints


class TestGetOrdersUser:

    @allure.title("Получение заказов конкретного пользователя: авторизованный пользователь")
    def test_get_orders_user_with_authorization(self, register_new_user_return_response):
        data = register_new_user_return_response
        access_token = data.json()["accessToken"]
        response = requests.get(f'{Urls.URL_SB}{Endpoints.GET_ORDERS_USER}', headers={'Authorization': f'{access_token}'})
        orders = response.json()["orders"]
        total = response.json()["total"]
        total_today = response.json()["totalToday"]
        assert response.status_code == 200 and response.text == f'{{"success":true,"orders":{orders},"total":{total},"totalToday":{total_today}}}'

    @allure.title("Получение заказов конкретного пользователя: неавторизованный пользователь")
    def test_get_orders_user_with_authorization(self):
        response = requests.get(f'{Urls.URL_SB}{Endpoints.GET_ORDERS_USER}')
        assert response.status_code == 401 and response.text == '{"success":false,"message":"You should be authorised"}'


