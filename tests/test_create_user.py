import pytest
import allure
import requests

from src.handlers import BaseURLs, UserAPIPaths, HTTPHeaders
from src.data import User


@allure.suite('Создание пользователя')
class TestCreateUser:

    @allure.description('Создание уникального пользователя')
    @allure.title('Создание уникального пользователя')
    def test_create_new_user_success(self):
        response = requests.post(f'{BaseURLs.STELLAR_BURGERS}{UserAPIPaths.REGISTER_USER}', data=User.generate_user_data())
        assert response.status_code == 200 and response.json()["success"] is True

        @allure.description('Создание пользователя, который уже зарегистрирован')
        @allure.title('Создание пользователя, который уже зарегистрирован')
        def test_create_duplicate_user_error(self):
            response = requests.post(f'{Urls.MAIN_URL}{Handlers.CREATE_USER}', data=User.duplicate_user_data)
            assert response.status_code == 403 and 'User already exists' in response.text

    @allure.description('Создание пользователя с некорректными данными')
    @allure.title('Создание пользователя с некорректными данными')
    @pytest.mark.parametrize("user_data", [User.data_missing_email, User.data_missing_password, User.data_missing_name])
    def test_create_user_incorrect_data(self, user_data):
        response = requests.post(f'{BaseURLs.STELLAR_BURGERS}{UserAPIPaths.REGISTER_USER}', data=user_data)
        assert response.status_code == 403 and 'Email, password and name are required fields' in response.text


