import allure
from helpers import generate_courier_data  # импорт уже есть

@allure.story('Создание курьера')
class TestCourierCreation:
    
    @allure.title('Создание курьера с заполнением обязательных полей')
    def test_courier_creation_success(self, courier_api):
        courier_data = generate_courier_data()
        response = courier_api.create_courier(courier_data)
        assert response.status_code == 201
        assert response.json() == {"ok": True}
        
        # 2. ДОБАВИТЬ: удаление созданного курьера
        login_response = courier_api.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            # Отправляем DELETE-запрос на удаление
            courier_api.api_client.delete(f'/api/v1/courier/{courier_id}')

    @allure.title('Создание дубликата курьера')
    def test_create_duplicate_courier(self, courier_api, created_courier):  
        
        # 5. ИСПОЛЬЗОВАТЬ данные из фикстуры
        existing_data = created_courier["data"]
        response = courier_api.create_courier(existing_data)
        assert response.status_code == 409
        assert response.json()['message'] == "Этот логин уже используется. Попробуйте другой."
        # Курьер удалится автоматически после теста (фикстура created_courier)

    @allure.title('Создание курьера с недостаточными данными')
    def test_create_courier_missing_one_field(self, courier_api):
        
        courier_data = generate_courier_data()
        del courier_data['password']
        response = courier_api.create_courier(courier_data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
        # Курьер не создан, удалять нечего