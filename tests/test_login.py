import allure
import requests

from src.handlers import BaseURLs, UserAPIPaths, HTTPHeaders
from src.data import User

@allure.suite('Логин пользователя')
class TestLogin:

    @allure.description('Логин под существующим пользователем')
    @allure.title('Логин под существующим пользователем')
    def test_login_user(self):
        response = requests.post(
            f"{BaseURLs.STELLAR_BURGERS}{UserAPIPaths.USER_LOGIN}",
            json=User.valid_data,
            headers=HTTPHeaders.JSON_HEADER
        )
        assert response.status_code == 200 and response.json().get('success') is True

    @allure.description('Логин с неверным логином и паролем')
    @allure.title('Логин с неверным логином и паролем')
    def test_login_user_error(self):
        response = requests.post(
            f"{BaseURLs.STELLAR_BURGERS}{UserAPIPaths.USER_LOGIN}",
            json=User.invalid_data,
            headers=HTTPHeaders.JSON_HEADER
        )
        assert response.status_code == 401 and response.json().get('success') is False
