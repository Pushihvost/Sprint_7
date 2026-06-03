import allure
import requests
from urls import BASE_URL

class OrderApi:

    @allure.step("Создаём тело запроса для заказа")
    def create_order(self, color):
        
        payload = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": color
    
    }
        response = requests.post(
                    f"{BASE_URL}/api/v1/orders",
                    json=payload
                )
        
        return response

