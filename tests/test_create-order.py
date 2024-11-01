import allure
import requests
from src.handlers import BaseURLs, UserAPIPaths, OrderAPIPaths, HTTPHeaders
from src.ingredients import Ingredient


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.description("С авторизацией")
    @allure.title("С авторизацией")
    def test_create_order_with_auth(self, create_user):
        token = {'Authorization': create_user[3]}
        response = requests.post(
            f"{BaseURLs.STELLAR_BURGERS}{OrderAPIPaths.PLACE_ORDER}",
            headers=token,
            json=Ingredient.correct_ingredients_data)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.description("Без авторизации")
    @allure.title("Без авторизации")
    def test_create_order_not_auth(self):
        response = requests.post(
            f"{BaseURLs.STELLAR_BURGERS}{OrderAPIPaths.PLACE_ORDER}",
            headers=HTTPHeaders.JSON_HEADER,
            json=Ingredient.correct_ingredients_data)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.description("С ингредиентами")
    @allure.title("С ингредиентами")
    def test_create_order_with_ingredients(self, create_user):
        token = {'Authorization': create_user[3]}
        response = requests.post(
            f"{BaseURLs.STELLAR_BURGERS}{OrderAPIPaths.PLACE_ORDER}",
            headers=token,
            json=Ingredient.correct_ingredients_data)
        assert response.json().get("success") is True

    @allure.description("Без ингредиентов")
    @allure.title("Без ингредиентов")
    def test_create_order_without_ingredients(self):
        r = requests.post(
            f"{BaseURLs.STELLAR_BURGERS}{OrderAPIPaths.PLACE_ORDER}"
        )
        assert r.status_code == 400 and r.json()['message'] == "Ingredient ids must be provided"

    @allure.description("С неверным хешем ингредиентов")
    @allure.title("С неверным хешем ингредиентов")
    def test_create_order_invalid_hash_ingredient(self):
        response = requests.post(
            f"{BaseURLs.STELLAR_BURGERS}{OrderAPIPaths.PLACE_ORDER}",
            headers=HTTPHeaders.JSON_HEADER,
            json=Ingredient.incorrect_ingredients_data
        )
        assert response.status_code == 500 and 'Internal Server Error' in response.text




