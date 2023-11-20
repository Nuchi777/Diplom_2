import allure
import pytest
import requests
from data import Urls
from data import Endpoints

class TestCreateUser:
    @allure.title(
        'Регистрация в приложении пройдет неуспешно, если повторно создать пользователя с теми же параметрами')
    def test_cannot_create_two_identical_couriers(self, new_courier_return_login_password):
        data = new_courier_return_login_password
        login = data[0]
        password = data[1]
        firstName = data[2]
        data_create = {
            "login": login,
            "password": password,
            "firstName": firstName
        }
        response = requests.post(f'{Urls.URL_SCOOTER}{Endpoints.CREATE_COURIER}', data=data_create)
        assert response.status_code == 409 and response.text == '{"message": "Этот логин уже используется"}'