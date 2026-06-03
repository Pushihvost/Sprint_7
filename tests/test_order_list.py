import allure
import requests
import pytest
from api.order_api import OrderApi
from urls import BASE_URL

class TestOrderList:

    @allure.title("Проверка получения заказа")
    @allure.step("Тест: Получить в ответ список заказов")
    def test_get_order_list(self):

         order_response = requests.get(
            f"{BASE_URL}/api/v1/orders"            
        )

         assert order_response.status_code == 200
         assert "orders" in order_response.json()

