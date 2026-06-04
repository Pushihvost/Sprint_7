import allure
import requests
import pytest
from api.courier_api import CourierApi
from urls import BASE_URL

class TestLoginCourier:
    
    @allure.title("Проверка Логина курьера")
    @allure.step("Тест: успешный вход с правильными кредами")
    def test_login_courier_successful(self, cleanup_courier, created_courier):

        payload = created_courier

        
        login_payload = {
    "login": payload["login"],
    "password": payload["password"]
        }
        with allure.step('Запрос на логин курьера с правильными полями'):
            login_response = requests.post(
                f"{BASE_URL}/api/v1/courier/login",
                data=login_payload
            )

            login_body = login_response.json()

            assert login_response.status_code == 200
            assert "id" in login_body
            assert login_body["id"] is not None

            courier_id = login_body.get("id")

            cleanup_courier.append(courier_id)

    @allure.title("Тест: логин с неверным логином или паролем")
    def test_login_courier_incorrect_login_or_password(self, cleanup_courier, created_courier):
        
        payload = created_courier
        
        
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
            with allure.step('Запрос на логин курьера с неправильными полями'):
                response = requests.post(
                    f"{BASE_URL}/api/v1/courier/login",
                    data=login_payload
                )

                body = response.json()

                assert response.status_code == 404
                assert body["message"] == "Учетная запись не найдена"

                courier_id = body.get("id")
                cleanup_courier.append(courier_id)

    @allure.title("Тест: логин с отсутствующим логином ил паролем")
    def test_login_courier_no_have_login_or_password(self, cleanup_courier, created_courier):
        
        payload = created_courier
        
        
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
            with allure.step('Запрос на логин курьера с отсутсвующим полем'):
                response = requests.post(
                    f"{BASE_URL}/api/v1/courier/login",
                    data=login_payload
                )

                body = response.json()

                assert response.status_code == 400
                assert body["message"] == "Недостаточно данных для входа"  
            
                courier_id = body.get("id")
                cleanup_courier.append(courier_id)
