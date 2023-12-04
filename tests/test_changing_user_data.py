import allure
import pytest
import requests
from data import Urls, Endpoints
from faker import Faker

faker = Faker()


class TestChangingUserData:


    """В классе TestChangingUserData я применил параметризацию, чтобы проверить,
    что можно изменить поля "name" и "email", чтобы не создавать разные тесты."""


    @pytest.mark.parametrize('payload_data', [f'{{"name": "{faker.first_name()}"}}', f'{{"email": "{faker.free_email()}"}}'])
    @allure.title("Изменение данных пользователя с авторизацией")
    def test_changing_user_data_with_authorization(self, register_new_user_return_response, payload_data):
        data = register_new_user_return_response
        access_token = data.json()["accessToken"]
        payload = payload_data
        response = requests.patch(f'{Urls.URL_SB}{Endpoints.UPDATE_USER}', data=payload, headers={'Authorization': f'{access_token}'})
        email = response.json()["user"]["email"]
        name = response.json()["user"]["name"]
        assert response.status_code == 200 and response.text == f'{{"success":true,"user":{{"email":"{email}","name":"{name}"}}}}'

    @pytest.mark.parametrize('payload_data',
                             [f'{{"name": "{faker.first_name()}"}}', f'{{"email": "{faker.free_email()}"}}'])
    @allure.title("Изменение данных пользователя без авторизации")
    def test_changing_user_data_without_authorization(self, payload_data):
        payload = payload_data
        response = requests.patch(f'{Urls.URL_SB}{Endpoints.UPDATE_USER}', data=payload)
        assert response.status_code == 401 and response.text == '{"success":false,"message":"You should be authorised"}'

