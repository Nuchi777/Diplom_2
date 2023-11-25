import allure
import requests
from data import Urls, Endpoints


class TestCreateOrder:
    @allure.suite("Создание заказа:")
    @allure.title("Создание заказа с авторизацией")
    def test_changing_user_data_with_authorization(self, register_new_user_return_response):
        data = register_new_user_return_response
        access_token = data.json()["accessToken"]
        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d"]
        }
        response = requests.post(f'{Urls.URL_SB}{Endpoints.CREATE_ORDER}', data=payload, headers={'Authorization': f'{access_token}'})
        name = response.json()["name"]
        order_number = response.json()["order"]["number"]
        print(response.text)
        # assert response.status_code == 200 and response.text == f'{{"name":"{name}","order":{{"number":{order_number}}},"success":true}}'

    @allure.title("Создание заказа с авторизацией")
    def test_changing_user_data_with_authorization(self, register_new_user_return_response):
        data = register_new_user_return_response
        access_token = data.json()["accessToken"]
        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d"]
        }
        response = requests.post(f'{Urls.URL_SB}{Endpoints.CREATE_ORDER}', data=payload)
        name = response.json()["name"]
        order_number = response.json()["order"]["number"]
        assert response.status_code == 200 and response.text == f'{{"name":"{name}","order":{{"number":{order_number}}},"success":true}}'

