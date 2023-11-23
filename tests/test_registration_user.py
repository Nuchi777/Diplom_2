import allure
import requests
from faker import Faker
from data import Urls
from data import Endpoints

faker = Faker()


class TestRegistrationUser:
    @allure.suite("Создание пользователя:")
    @allure.title("Создать уникального пользователя")
    def test_registration_new_user(self, register_new_user_return_response):
        response = register_new_user_return_response
        email = response.json()["user"]["email"]
        name = response.json()["user"]["name"]
        access_token = response.json()["accessToken"]
        refresh_token = response.json()["refreshToken"]
        assert response.status_code == 200 and response.text == f'{{"success":true,"user":{{"email":"{email}","name":"{name}"}},"accessToken":"{access_token}","refreshToken":"{refresh_token}"}}'

@allure.title('Создать уникального пользователя')
    def test_registration_new_user(self, user):
        data = user
        email = data[0]
        password = data[1]
        name = data[2]
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(f'{Urls.URL_SB}{Endpoints.REGISTRATION_USER}', data=payload)
        access_token = response.json()["accessToken"]
        refresh_token = response.json()["refreshToken"]
        assert response.status_code == 200 and response.text == f'{{"success":true,"user":{{"email":"{email}","name":"{name}"}},"accessToken":"{access_token}","refreshToken":"{refresh_token}"}}'
