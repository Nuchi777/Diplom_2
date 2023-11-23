import allure
import requests
from faker import Faker
from data import Urls
from data import Endpoints

faker = Faker()


class TestRegistrationUser:
    @allure.suite("Создание пользователя:")
    @allure.title("Создать уникального пользователя")
    def test_register_new_user(self, register_new_user_return_response):
        response = register_new_user_return_response
        email = response.json()["user"]["email"]
        name = response.json()["user"]["name"]
        access_token = response.json()["accessToken"]
        refresh_token = response.json()["refreshToken"]
        assert response.status_code == 200 and response.text == f'{{"success":true,"user":{{"email":"{email}","name":"{name}"}},"accessToken":"{access_token}","refreshToken":"{refresh_token}"}}'

    @allure.title('Создать пользователя, который уже зарегистрирован')
    def test_register_user_which_already_registered(self, register_new_user_return_login_pass):
        data = register_new_user_return_login_pass
        email = data[0]
        password = data[1]
        name = data[2]
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(f'{Urls.URL_SB}{Endpoints.REGISTRATION_USER}', data=payload)
        assert response.status_code == 403 and response.text == f'{{"success":false,"message":"User already exists"}}'

    @allure.title('Создать пользователя и не заполнить одно из обязательных полей.')
    def test_register_user_not_fill_required_fields(self):
        email = faker.free_email()
        name = faker.first_name()
        payload = {
            "email": email,
            "password": "",
            "name": name
        }
        response = requests.post(f'{Urls.URL_SB}{Endpoints.REGISTER_USER}', data=payload)
        assert response.status_code == 403 and response.text == f'{{"success":false,"message":"Email, password and name are required fields"}}'


