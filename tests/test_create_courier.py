import allure
import requests
import pytest
from api.courier_api import CourierApi
from urls import BASE_URL

class TestCreateCourier:

    @allure.title("Проверки на создание курьера")
    @allure.step("Тест: успешное создание курьера")
    def test_create_courier_first_successful(self, cleanup_courier):
        courier_api = CourierApi()
        response, payload = courier_api.register_new_courier_and_return_response()

        body = response.json()

        assert response.status_code == 201 
        assert body["ok"] is True

        courier_id = courier_api.login_courier_and_return_id(payload)
        cleanup_courier.append(courier_id)

    @allure.step("Тест: нельзя создать двух одинаковых курьеров")
    def test_create_courier_twice_fail(self, cleanup_courier):
        courier_api = CourierApi()
        response, payload = courier_api.register_new_courier_and_return_response()

        with allure.step('Запрос на повторное создание курьера'):
            response2 = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)

            body = response2.json()

            assert response2.status_code == 409
            assert body["message"] == "Этот логин уже используется. Попробуйте другой."

            courier_id = courier_api.login_courier_and_return_id(payload)
            cleanup_courier.append(courier_id)
    
    @allure.step("Тест: если одного из полей нет, запрос возвращает ошибку")
    @pytest.mark.parametrize("payload", [
        {"login": "user2222", "firstName": "Bob"},
        {"password": "pass123", "firstName": "John"},
        {"login": "user2222"}
    ])
    def test_create_courier_incorrect_headers_fail(self, payload):

        with allure.step('Запрос на создание курьера без обязательного поля'):
            response = requests.post(
                f"{BASE_URL}/api/v1/courier",
                data=payload
            )

            body = response.json()

            assert response.status_code == 400
            assert body["message"] == "Недостаточно данных для создания учетной записи"










