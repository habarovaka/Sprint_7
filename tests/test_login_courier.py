import pytest
import allure
from api_client import ScooterApiClient


class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_success_login(self, courier):
        with allure.step("Подготовка данных для авторизации (использование фикстуры)"):
            payload = {"login": courier["login"], "password": courier["password"]}
        with allure.step("Отправка запроса на авторизацию"):
            response = ScooterApiClient.login_courier(payload)
        with allure.step("Проверка статус-кода (200) и наличия ID"):
            assert response.status_code == 200
            assert "id" in response.json()

    @allure.title("Ошибка авторизации при отсутствии обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_missing_field(self, courier, missing_field):
        with allure.step("Подготовка данных с удалением обязательного поля"):
            payload = {"login": courier["login"], "password": courier["password"]}
            del payload[missing_field]
        with allure.step("Отправка запроса на авторизацию с неполными данными"):
            response = ScooterApiClient.login_courier(payload)
        with allure.step("Проверка статус-кода (400) и сообщения об ошибке"):
            assert response.status_code == 400
            assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Ошибка авторизации с неправильными данными")
    def test_login_with_wrong_credentials(self, courier):
        with allure.step("Подготовка данных с неверным паролем"):
            payload = {"login": courier["login"], "password": "wrong_password_123"}
        with allure.step("Отправка запроса на авторизацию"):
            response = ScooterApiClient.login_courier(payload)
        with allure.step("Проверка статус-кода (404) и сообщения об ошибке"):
            assert response.status_code == 404
            assert response.json()["message"] == "Учетная запись не найдена"