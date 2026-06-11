import pytest
from api_client import ScooterApiClient
from data_helper import generate_courier_data


@pytest.fixture
def courier():
    courier_data = generate_courier_data()
    ScooterApiClient.create_courier(courier_data)
    yield courier_data
    login_res = ScooterApiClient.login_courier({"login": courier_data["login"], "password": courier_data["password"]})
    if login_res.status_code == 200:
        courier_id = login_res.json().get("id")
        ScooterApiClient.delete_courier(courier_id)