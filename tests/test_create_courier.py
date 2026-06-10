import pytest
import allure
from api_client import ScooterApiClient
from data_helper import generate_courier_data


class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_success_create_courier(self):
        payload = generate_courier_data()
        response = ScooterApiClient.create_courier(payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}
        login_res = ScooterApiClient.login_courier({"login": payload["login"], "password": payload["password"]})
        if login_res.status_code == 200:
            courier_id = login_res.json().get("id")
            ScooterApiClient.delete_courier(courier_id)

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_cannot_create_duplicate_courier(self):
        payload = generate_courier_data()
        ScooterApiClient.create_courier(payload)
        res2 = ScooterApiClient.create_courier(payload)
        assert res2.status_code == 409
        assert res2.json()["message"] == "Этот логин уже используется. Попробуйте другой."
        login_res = ScooterApiClient.login_courier({"login": payload["login"], "password": payload["password"]})
        if login_res.status_code == 200:
            courier_id = login_res.json().get("id")
            ScooterApiClient.delete_courier(courier_id)

    @allure.title("Ошибка при отсутствии обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_required_field(self, missing_field):
        payload = generate_courier_data()
        del payload[missing_field]
        response = ScooterApiClient.create_courier(payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"