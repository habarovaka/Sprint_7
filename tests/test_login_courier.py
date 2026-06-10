import pytest
import allure
from api_client import ScooterApiClient


class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_success_login(self, courier):
        payload = {"login": courier["login"], "password": courier["password"]}
        response = ScooterApiClient.login_courier(payload)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Ошибка авторизации при отсутствии обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_missing_field(self, courier, missing_field):
        payload = {"login": courier["login"], "password": courier["password"]}
        del payload[missing_field]
        response = ScooterApiClient.login_courier(payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Ошибка авторизации с неправильными данными")
    def test_login_with_wrong_credentials(self, courier):
        payload = {"login": courier["login"], "password": "wrong_password_123"}
        response = ScooterApiClient.login_courier(payload)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"