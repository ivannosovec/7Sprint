import allure
import pytest
from helpers import generate_courier_data


@allure.story('Создание заказа')
class TestOrderCreation:
    @pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    @allure.title('Создание заказа с указанием цвета: {colors}')
    def test_successful_order_creation(self, api_client, order_api, colors):
        order_data = {
            "firstName": "Ivan",
            "lastName": "Nosovets",
            "address": "Moscow",
            "metroStation": "3",
            "phone": "+7 999 535 50 20",
            "rentTime": 5,
            "deliveryDate": "2024-07-01",
            "comment": "Как можно быстрее",
            "color": colors
        }
        response = order_api.create_order(order_data)
        assert response.status_code == 201
        assert "track" in response.json()