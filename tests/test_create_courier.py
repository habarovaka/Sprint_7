import pytest
import allure
from api_client import ScooterApiClient
from data_helper import generate_courier_data


class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_success_create_courier(self):
        with allure.step("Генерация случайных данных курьера"):
            payload = generate_courier_data()
        with allure.step("Вызов API создания курьера"):
            response = ScooterApiClient.create_courier(payload)
        with allure.step("Проверка статус-кода и тела ответа"):
            assert response.status_code == 201
            assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_cannot_create_duplicate_courier(self):
        with allure.step("Генерация данных курьера"):
            payload = generate_courier_data()
        with allure.step("Создание первого курьера"):
            ScooterApiClient.create_courier(payload)
        with allure.step("Попытка создания курьера с таким же логином"):
            res2 = ScooterApiClient.create_courier(payload)
        with allure.step("Проверка статус-кода ошибки 409 и сообщения"):
            assert res2.status_code == 409
            assert res2.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Ошибка при отсутствии обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_required_field(self, missing_field):
        with allure.step("Генерация базовых данных курьера"):
            payload = generate_courier_data()
        with allure.step(f"Удаление обязательного поля: {missing_field}"):
            del payload[missing_field]
        with allure.step("Отправка запроса с неполными данными"):
            response = ScooterApiClient.create_courier(payload)
        with allure.step("Проверка статус-кода ошибки 400 и сообщения"):
            assert response.status_code == 400
            assert response.json()["message"] == "Недостаточно данных для создания учетной записи"