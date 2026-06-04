import allure
import requests
import random
import string
from urls import BASE_URL

class CourierApi:

    @allure.step("Генерация рандомных данных для формы")
    def generate_random_string(self, length):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(length))

    @allure.step("Создаём тело запроса для авторизации")
    def create_courier_payload(self):
        return {
            "login": self.generate_random_string(12),
            "password": self.generate_random_string(10),
            "firstName": self.generate_random_string(12)
        }
    @allure.step("Создаём курьера")
    def register_new_courier_and_return_response(self):
        payload = self.create_courier_payload()

        response = requests.post(
            f"{BASE_URL}/api/v1/courier",
            data=payload
        )

        return response, payload

    @allure.step("Удаляем курьера")
    def delete_courier_and_return_response(self, id_courier):
        response = requests.delete(
    f"{BASE_URL}/api/v1/courier/{id_courier}"
)
        return response
    
    @allure.step("Логин курьера")
    def login_courier_and_return_id(self, payload):
        
        login_payload = {
    "login": payload["login"],
    "password": payload["password"]
        }
        
        login_response = requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            data=login_payload
        )

        login_body = login_response.json()

        return login_body.get("id")


