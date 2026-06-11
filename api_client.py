import requests
import allure
from urls import Urls


class ScooterApiClient:

    @staticmethod
    @allure.step("Отправка запроса на создание курьера")
    def create_courier(payload):
        return requests.post(Urls.CREATE_COURIER, json=payload)

    @staticmethod
    @allure.step("Отправка запроса на авторизацию курьера")
    def login_courier(payload):
        return requests.post(Urls.LOGIN_COURIER, json=payload)

    @staticmethod
    @allure.step("Отправка запроса на удаление курьера")
    def delete_courier(courier_id):
        return requests.delete(f"{Urls.DELETE_COURIER}{courier_id}")

    @staticmethod
    @allure.step("Отправка запроса на создание заказа")
    def create_order(payload):
        return requests.post(Urls.ORDERS, json=payload)

    @staticmethod
    @allure.step("Отправка запроса на получение списка заказов")
    def get_orders_list():
        return requests.get(Urls.ORDERS)