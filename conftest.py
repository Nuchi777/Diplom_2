import pytest
import requests
from register_new_user import register_new_user
from data import Urls, Endpoints


@pytest.fixture
def register_new_user_return_login_pass():
    data = register_new_user()
    yield data[0]

    endpoint_delete_courier = f'/api/v1/courier/{id_courier}'
    requests.delete(f'{url}{endpoint_delete_courier}')


@pytest.fixture
def register_new_user_return_response():
    data = register_new_user()
    yield data[1]
    access_token = data[1].json()["accessToken"]
    requests.delete(f'{Urls.URL_SB}{Endpoints.DELETE_USER}', headers={'Authorization': f'{access_token}'})
