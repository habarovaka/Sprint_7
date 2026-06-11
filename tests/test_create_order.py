import pytest
import allure
import copy
from api_client import ScooterApiClient
from data_helper import BASE_ORDER_PAYLOAD


class TestCreateOrder:

    @allure.title("Создание заказа с различными цветами")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_different_colors(self, color):
        with allure.step("Получение базового шаблона данных заказа"):
            order_payload = copy.deepcopy(BASE_ORDER_PAYLOAD)

        with allure.step(f"Добавление выбранного цвета {color} в параметры"):
            order_payload["color"] = color

        with allure.step("Отправка запроса на создание заказа"):
            response = ScooterApiClient.create_order(order_payload)

        with allure.step("Проверка успешного создания (201) и наличия трек-номера"):
            assert response.status_code == 201
            assert "track" in response.json()