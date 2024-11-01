import allure
import requests

from src.handlers import BaseURLs, OrderAPIPaths, HTTPHeaders
from src.ingredients import Ingredient

@allure.suite("Получение заказов конкретного пользователя")
class TestGetOrderUser:

    @allure.description("Авторизованный пользователь")
    @allure.title("Авторизованный пользователь")
    def test_get_order_user_with_auth(self, create_user):
        token = {'Authorization': create_user[3]}
        requests_create_order = requests.post(
            f"{BaseURLs.STELLAR_BURGERS}{OrderAPIPaths.PLACE_ORDER}",
            headers=token,
            json=Ingredient.correct_ingredients_data
        )
        response_get_order = requests.get(
            f"{BaseURLs.STELLAR_BURGERS}{OrderAPIPaths.VIEW_USER_ORDERS}",
            headers=token
        )
        assert response_get_order.status_code == 200, (
            f"Expected status code 200 for getting orders, got {response_get_order.status_code}. "
            f"Create Order Response: {requests_create_order.text}, "
            f"Get Orders Response: {response_get_order.text}"
        )

    @allure.description("Неавторизованный пользователь")
    @allure.title("Неавторизованный пользователь")
    def test_get_order_user_not_auth(self):
        r = requests.get(f"{BaseURLs.STELLAR_BURGERS}{OrderAPIPaths.VIEW_USER_ORDERS}")
        assert r.status_code == 401 and r.json()['message'] == "You should be authorised"


