import requests
from urls import Urls


class ScooterApiClient:

    @staticmethod
    def create_courier(payload):
        return requests.post(Urls.CREATE_COURIER, json=payload)

    @staticmethod
    def login_courier(payload):
        return requests.post(Urls.LOGIN_COURIER, json=payload)

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f"{Urls.DELETE_COURIER}{courier_id}")

    @staticmethod
    def create_order(payload):
        return requests.post(Urls.ORDERS, json=payload)

    @staticmethod
    def get_orders_list():
        return requests.get(Urls.ORDERS)