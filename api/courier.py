import allure


class CourierApi:
    def __init__(self, api_client):
        self.api_client = api_client
        self.courier_id = None

    @allure.step('Создание курьера')
    def create_courier(self, courier_data):
        return self.api_client.post('/api/v1/courier', data=courier_data)

    @allure.step('Авторизация курьера')
    def login_courier(self, data):
        response = self.api_client.post('/api/v1/courier/login', data=data)
        if response.status_code == 200:
            self.courier_id = response.json().get("id")
        return response

    # ⛔️ Метод generation_courier_data удалён из класса

    @allure.step('Получение ID курьера')
    def get_courier_id(self):
        return self.courier_id