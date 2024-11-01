import pytest
import requests
from src.handlers import BaseURLs, UserAPIPaths, HTTPHeaders
from src.data import User


@pytest.fixture(scope="function")
def create_user():
    payload = User.generate_user_data()
    login_data = payload.copy()
    del login_data["name"]
    response = requests.post(f"{BaseURLs.STELLAR_BURGERS}{UserAPIPaths.REGISTER_USER}", json=payload)
    token = response.json()["accessToken"]
    yield response, payload, login_data, token
    requests.delete(f"{BaseURLs.STELLAR_BURGERS}{UserAPIPaths.REMOVE_USER}", headers={'Authorization': f'{token}'})
