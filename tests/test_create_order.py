import allure
import requests
from data import Urls, Endpoints


class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_authorization(self, register_new_user_return_response):
        data = register_new_user_return_response
        access_token = data.json()["accessToken"]
        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d"]
        }
        response = requests.post(f'{Urls.URL_SB}{Endpoints.CREATE_ORDER}', data=payload, headers={'Authorization': f'{access_token}'})
        assert response.status_code == 200
        # в документации нет примера ответа для авторизованного пользователя

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_authorization(self):
        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d"]
        }
        response = requests.post(f'{Urls.URL_SB}{Endpoints.CREATE_ORDER}', data=payload)
        name = response.json()["name"]
        order_number = response.json()["order"]["number"]
        assert response.status_code == 200 and response.text == f'{{"name":"{name}","order":{{"number":{order_number}}},"success":true}}'

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, register_new_user_return_response):
        data = register_new_user_return_response
        access_token = data.json()["accessToken"]
        payload = {
            "ingredients": [""]
        }
        response = requests.post(f'{Urls.URL_SB}{Endpoints.CREATE_ORDER}', data=payload, headers={'Authorization': f'{access_token}'})
        assert response.status_code == 400 and response.text == '{"success":false,"message":"Ingredient ids must be provided"}'

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_ingredient_hash(self, register_new_user_return_response):
        data = register_new_user_return_response
        access_token = data.json()["accessToken"]
        payload = {
            "ingredients": ["60d3b41abdacab0026a733c6"]
        }
        response = requests.post(f'{Urls.URL_SB}{Endpoints.CREATE_ORDER}', data=payload, headers={'Authorization': f'{access_token}'})
        assert response.status_code == 500


