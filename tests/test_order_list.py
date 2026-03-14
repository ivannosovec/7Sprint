import allure


@allure.story('Получение списка заказов')
class TestOrderList:
    @allure.title('Получение списка заказов с некорректным courierId')
    def test_get_list_order_with_defunct_courier_id(self, order_api):
        defunct_courier_id = 111111111
        response = order_api.get_orders(courierId=defunct_courier_id)
        assert response.status_code == 404
        assert response.json()["message"] == f"Курьер с идентификатором {defunct_courier_id} не найден"

    @allure.title('Получение списка заказов с существующим courierId')
    def test_get_list_order_with_exists_courier_id(self, order_api):
        response = order_api.get_orders()
        orders = response.json().get('orders', [])
        assert response.status_code == 200
        assert len(orders) > 0, "Список заказов пустой"