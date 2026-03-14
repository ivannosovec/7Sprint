import allure

@allure.story('Создание курьера')
class TestCourierCreation:
    @allure.title('Создание курьера с заполнением обязательных полей')
    def test_courier_creation_success(self, courier_api):
        courier_data = courier_api.generation_courier_data()
        response = courier_api.create_courier(courier_data)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Создание дубликата курьера')
    def test_create_duplicate_courier(self, courier_api):
        courier_data = courier_api.generation_courier_data()
        courier_api.create_courier(courier_data)
        response = courier_api.create_courier(courier_data)
        assert response.status_code == 409
        assert response.json()['message'] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Создание курьера с недостаточными данными')
    def test_create_courier_missing_one_field(self, courier_api):
        courier_data = courier_api.generation_courier_data()
        del courier_data['password']
        response = courier_api.create_courier(courier_data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"