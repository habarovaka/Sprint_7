import pytest
import allure
from api_client import ScooterApiClient


class TestCreateOrder:

    @allure.title("Создание заказа с различными цветами")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_different_colors(self, color):
        order_payload = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "address": "Москва",
            "metroStation": 4,
            "phone": "+79991112233",
            "rentTime": 5,
            "deliveryDate": "2026-12-31",
            "comment": "Тест",
            "color": color
        }
        response = ScooterApiClient.create_order(order_payload)
        assert response.status_code == 201
        assert "track" in response.json()