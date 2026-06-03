import allure
import requests
import pytest
from api.courier_api import CourierApi
from urls import BASE_URL

class TestLoginCourier:
    
    @allure.title("Проверка Логина курьера")
    @allure.step("Тест: успешный вход с правильными кредами")
    def test_login_courier_successful(self):
        courier_api = CourierApi()
        response, payload = courier_api.register_new_courier_and_return_response()
        
        login_payload = {
    "login": payload["login"],
    "password": payload["password"]
        }

        login_response = requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            data=login_payload
        )

        login_body = login_response.json()

        assert login_response.status_code == 200
        assert "id" in login_body
        assert login_body["id"] is not None

    @allure.title("Тест: логин с неверным логином или паролем")
    def test_login_courier_incorrect_login_or_password(self):
        
        courier_api = CourierApi()
        response, payload = courier_api.register_new_courier_and_return_response()
        
        invalid_payloads = [
            {
                "login": "bad_login",
                "password": payload["password"]
            },
            {
                "login": payload["login"],
                "password": "incorrect_password"
            }
        ]

        for login_payload in invalid_payloads:
            response = requests.post(
                f"{BASE_URL}/api/v1/courier/login",
                data=login_payload
            )

            body = response.json()

            assert response.status_code == 404
            assert body["message"] == "Учетная запись не найдена"

    @allure.title("Тест: логин с отсутствующим логином ил паролем")
    def test_login_courier_no_have_login_or_password(self):
        
        courier_api = CourierApi()
        response, payload = courier_api.register_new_courier_and_return_response()
        
        invalid_payloads = [
            {
                "login": "",
                "password": payload["password"]
            },
            {
                "login": payload["login"],
                "password": ""
            }
        ]

        for login_payload in invalid_payloads:
            response = requests.post(
                f"{BASE_URL}/api/v1/courier/login",
                data=login_payload
            )

            body = response.json()

            assert response.status_code == 400
            assert body["message"] == "Недостаточно данных для входа"      
