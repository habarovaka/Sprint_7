import random
import string

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_courier_data():
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }

BASE_ORDER_PAYLOAD = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": "Москва",
    "metroStation": 4,
    "phone": "+79991112233",
    "rentTime": 5,
    "deliveryDate": "2026-12-31",
    "comment": "Тест"
}