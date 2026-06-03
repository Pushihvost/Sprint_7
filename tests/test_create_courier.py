import allure
import requests
import pytest
from api.courier_api import CourierApi
from urls import BASE_URL

class TestCreateCourier:

    @allure.title("Проверки на создание курьера")
    @allure.step("Тест: успешное создание курьера")
    def test_create_courier_first_successful(self):
        courier_api = CourierApi()
        response, payload = courier_api.register_new_courier_and_return_response()

        body = response.json()

        assert response.status_code == 201 
        assert body["ok"] is True

    @allure.step("Тест: нельзя создать двух одинаковых курьеров")
    def test_create_courier_twice_fail(self):
        courier_api = CourierApi()
        response, payload = courier_api.register_new_courier_and_return_response()

        response2 = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)

        body = response2.json()

        assert response2.status_code == 409
        assert body["message"] == "Этот логин уже используется. Попробуйте другой."
    
    @allure.step("Тест: если одного из полей нет, запрос возвращает ошибку")
    @pytest.mark.parametrize("payload", [
        {"login": "user2222", "firstName": "Bob"},
        {"password": "pass123", "firstName": "John"},
        {"login": "user2222"}
    ])
    def test_create_courier_incorrect_headers_fail(self, payload):

        response = requests.post(
            f"{BASE_URL}/api/v1/courier",
            data=payload
        )

        body = response.json()

        assert response.status_code == 400
        assert body["message"] == "Недостаточно данных для создания учетной записи"










