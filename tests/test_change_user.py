import allure
import requests
from src.handlers import BaseURLs, UserAPIPaths, HTTPHeaders
from src.data import User


@allure.suite('Изменение данных пользовователя')
class TestChangingUserData:

    @allure.description("Успешное изменение email авторизованного пользователя")
    @allure.title("Успешное изменение email авторизованного пользователя")
    def test_changing_user_email_with_auth(self, create_user):
        payload = {'email': User.generate_user_data()["email"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{BaseURLs.STELLAR_BURGERS}{UserAPIPaths.UPDATE_USER_PROFILE}", headers=token, json=payload)
        assert r.status_code == 200 and r.json()['user']['email'] == payload["email"]

    @allure.description("Успешное изменение password авторизованного пользователя")
    @allure.title("Успешное изменение password авторизованного пользователя")
    def test_changing_user_password_with_auth(self, create_user):
        payload = {'password': User.generate_user_data()["password"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{BaseURLs.STELLAR_BURGERS}{UserAPIPaths.UPDATE_USER_PROFILE}", headers=token, json=payload)
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.description("Успешное изменение name авторизованного пользователя")
    @allure.title("Успешное изменение name авторизованного пользователя")
    def test_changing_user_name_with_auth(self, create_user):
        payload = {'name': User.generate_user_data()["name"]}
        token = {'Authorization': create_user[3]}
        r = requests.patch(f"{BaseURLs.STELLAR_BURGERS}{UserAPIPaths.UPDATE_USER_PROFILE}", headers=token, json=payload)
        assert r.status_code == 200 and r.json()['user']['name'] == payload["name"]

    @allure.description("Изменение данных пользователя без авторизации")
    @allure.title("Изменение данных пользователя без авторизации")
    def test_changing_user_data_not_auth(self):
        r = requests.patch(f"{BaseURLs.STELLAR_BURGERS}{UserAPIPaths.UPDATE_USER_PROFILE}", json=User.updated_user_data)
        assert r.status_code == 401 and r.json()['message'] == 'You should be authorised'

    @allure.description("Успешное изменение email неавторизованного пользователя")
    @allure.title("Успешное изменение email неавторизованного пользователя")
    def test_changing_user_email_without_auth(self):
        payload = {'email': User.generate_user_data()["email"]}
        r = requests.patch(f"{BaseURLs.STELLAR_BURGERS}{UserAPIPaths.UPDATE_USER_PROFILE}", json=payload)
        assert r.status_code == 401

    @allure.description("Успешное изменение password неавторизованного пользователя")
    @allure.title("Успешное изменение password неавторизованного пользователя")
    def test_changing_user_password_without_auth(self):
        payload = {'password': User.generate_user_data()["password"]}
        r = requests.patch(f"{BaseURLs.STELLAR_BURGERS}{UserAPIPaths.UPDATE_USER_PROFILE}", json=payload)
        assert r.status_code == 401

    @allure.description("Успешное изменение name неавторизованного пользователя")
    @allure.title("Успешное изменение name неавторизованного пользователя")
    def test_changing_user_name_without_auth(self):
        payload = {'name': User.generate_user_data()["name"]}
        r = requests.patch(f"{BaseURLs.STELLAR_BURGERS}{UserAPIPaths.UPDATE_USER_PROFILE}", json=payload)
        assert r.status_code == 401