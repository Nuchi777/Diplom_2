import requests
from faker import Faker
from data import Urls, Endpoints
from helpers import generate_random_string

faker = Faker()


def register_new_user_return_login_pass_and_response():
    # создаём список, чтобы функция могла его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    email = faker.free_email()
    password = generate_random_string(5)
    name = faker.first_name()

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на регистрацию нового пользователя и сохраняем ответ в переменную response
    response = requests.post(f'{Urls.URL_SB}{Endpoints.REGISTER_USER}', data=payload)

    # если регистрация прошла успешно (код ответа 200), добавляем в список email, пароль и имя пользователя
    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(name)

    # возвращаем список и ответ сервера
    return login_pass, response
