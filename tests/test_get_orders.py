import allure
from api_client import ScooterApiClient


class TestGetOrdersList:

    @allure.title("Получение списка всех заказов")
    def test_get_orders_list_returns_orders(self):
        with allure.step("Отправка запроса на получение списка заказов"):
            response = ScooterApiClient.get_orders_list()
        with allure.step("Проверка успешного статус-кода (200)"):
            assert response.status_code == 200
        with allure.step("Проверка, что в ответе есть список заказов"):
            assert "orders" in response.json()
            assert isinstance(response.json()["orders"], list)