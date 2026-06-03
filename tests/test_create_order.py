import allure
import requests
import pytest
from api.order_api import OrderApi


class TestCreateOrder:

    @allure.title("Проверка Создания заказа")
    @allure.step("Тест: можно указать один из цветов, оба цвета, совсем не указывать цвет; тело ответа содержит track ")
    @pytest.mark.parametrize("color", 
                             [
                                 ["Black"], 
                                 ["Grey"], 
                                 ["Black", "Grey"], 
                                 [""]
                             ])
    def test_create_order_different_color(self, color):
        
        order_api = OrderApi()

        response = order_api.create_order(color)

        body = response.json()

        assert response.status_code == 201
        assert "track" in body
        assert body["track"] is not None
