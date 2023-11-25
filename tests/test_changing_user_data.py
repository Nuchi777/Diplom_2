import allure
import requests
from data import Urls, Endpoints


class TestChangingUserData:
    @allure.suite("Изменение данных пользователя:")
    @allure.title("Изменение данных пользователя с авторизацией")
    def test_changing_user_data_with_authorization(self, register_new_user_return_response):
        data = register_new_user_return_response
        email = data.json()["user"]["email"]
        access_token = data.json()["accessToken"]
        payload = {"name": "Ivan Ivanov"}
        response = requests.patch(f'{Urls.URL_SB}{Endpoints.UPDATE_USER}', data=payload, headers={'Authorization': f'{access_token}'})
        assert response.status_code == 200 and response.text == f'{{"success":true,"user":{{"email":"{email}","name":"Ivan Ivanov"}}}}'

    @allure.title("Изменение данных пользователя без авторизации")
    def test_changing_user_data_without_authorization(self, register_new_user_return_response):
        payload = {"name": "Ivan Ivanov"}
        response = requests.patch(f'{Urls.URL_SB}{Endpoints.UPDATE_USER}', data=payload)
        assert response.status_code == 401 and response.text == '{"success":false,"message":"You should be authorised"}'

