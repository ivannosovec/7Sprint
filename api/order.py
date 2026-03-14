import allure
from api.base import ApiClient


class OrderApi:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    @allure.step('Отправка запроса на создание заказа')
    def create_order(self, data):
        return self.api_client.post('/api/v1/orders', data=data)

    @allure.step('Отправка запроса на получение заказа')
    def get_orders(self, courierId=None):
        params = {'courierId': courierId} if courierId is not None else {}
        return self.api_client.get('/api/v1/orders', params=params)