import allure
import requests
from faker import Faker
from data import Urls, Endpoints
from random import randint

faker = Faker()


class TestLoginUser:

    @allure.title("Логин под существующим пользователем")
    def test_login_registered_user(self, register_new_user_return_login_pass):
        data = register_new_user_return_login_pass
        email = data[0]
        password = data[1]
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(f'{Urls.URL_SB}{Endpoints.LOGIN_USER}', data=payload)
        email = response.json()["user"]["email"]
        name = response.json()["user"]["name"]
        access_token = response.json()["accessToken"]
        refresh_token = response.json()["refreshToken"]
        assert response.status_code == 200 and response.text == f'{{"success":true,"accessToken":"{access_token}","refreshToken":"{refresh_token}","user":{{"email":"{email}","name":"{name}"}}}}'

    @allure.title("Логин с неверным логином и верным паролем")
    def test_login_user_with_incorrect_username_and_correct_password(self, register_new_user_return_login_pass):
        data = register_new_user_return_login_pass
        email = faker.free_email()
        password = data[1]
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(f'{Urls.URL_SB}{Endpoints.LOGIN_USER}', data=payload)
        assert response.status_code == 401 and response.text == '{"success":false,"message":"email or password are incorrect"}'

    @allure.title("Логин с верным логином и неверным паролем")
    def test_login_user_with_correct_username_and_incorrect_password(self, register_new_user_return_login_pass):
        data = register_new_user_return_login_pass
        email = data[0]
        password = randint(100000, 999999)
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(f'{Urls.URL_SB}{Endpoints.LOGIN_USER}', data=payload)
        assert response.status_code == 401 and response.text == '{"success":false,"message":"email or password are incorrect"}'


