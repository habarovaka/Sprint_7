import allure
from api_client import ScooterApiClient


class TestGetOrdersList:

    @allure.title("Получение списка всех заказов")
    def test_get_orders_list_returns_orders(self):
        response = ScooterApiClient.get_orders_list()
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)