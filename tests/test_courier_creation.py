import allure
from helpers import generate_courier_data


@allure.story('Создание курьера')
class TestCourierCreation:
    
    @allure.title('Создание курьера с заполнением обязательных полей')
    def test_courier_creation_success(self, courier_api):
        # Генерируем данные
        courier_data = generate_courier_data()
        
        # Создаём курьера
        create_response = courier_api.create_courier(courier_data)
        assert create_response.status_code == 201
        assert create_response.json() == {"ok": True}
        
        # Логинимся для получения ID (обязательно должно быть успешно)
        login_response = courier_api.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        assert login_response.status_code == 200, "Не удалось залогиниться после создания"
        courier_id = login_response.json().get("id")
        assert courier_id is not None, "ID курьера не получен"
        
        # Удаляем курьера
        delete_response = courier_api.api_client.delete(f'/api/v1/courier/{courier_id}')
        assert delete_response.status_code == 200, "Не удалось удалить курьера"

    @allure.title('Создание дубликата курьера')
    def test_create_duplicate_courier(self, courier_api, created_courier):
        # Используем данные из фикстуры
        existing_data = created_courier["data"]
        
        # Пытаемся создать дубликат
        response = courier_api.create_courier(existing_data)
        assert response.status_code == 409
        assert response.json()['message'] == "Этот логин уже используется. Попробуйте другой."
        # Курьер удалится автоматически после теста (фикстура created_courier)

    @allure.title('Создание курьера с недостаточными данными')
    def test_create_courier_missing_one_field(self, courier_api):
        # Генерируем данные и удаляем обязательное поле
        courier_data = generate_courier_data()
        del courier_data['password']
        
        # Пытаемся создать курьера без пароля
        response = courier_api.create_courier(courier_data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
        # Курьер не создан, удалять нечего