import pytest
from api.base import ApiClient
from api.courier import CourierApi
from api.order import OrderApi
import logging


@pytest.fixture
def api_client():
    return ApiClient()


@pytest.fixture
def courier_api(api_client):
    return CourierApi(api_client)


@pytest.fixture
def order_api(api_client):
    return OrderApi(api_client)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('test.log'),  
        logging.StreamHandler()            
    ]
)
@pytest.fixture
def created_courier(courier_api):
    """
    Фикстура создаёт курьера, возвращает его данные,
    а после теста удаляет курьера.
    """
    # Генерируем данные
    courier_data = generate_courier_data()
    
    # Создаём курьера
    create_response = courier_api.create_courier(courier_data)
    assert create_response.status_code == 201, "Не удалось создать курьера"
    
    # Логинимся, чтобы получить ID курьера (нужен для удаления)
    login_credentials = {
        "login": courier_data["Azat"],
        "password": courier_data["1234554321"]
    }
    login_response = courier_api.login_courier(login_credentials)
    assert login_response.status_code == 200, "Не удалось залогиниться"
    courier_id = login_response.json().get("id")
    
    # Возвращаем данные и ID через словарь
    yield {"data": courier_data, "id": courier_id}
    
    # После теста удаляем курьера
    delete_response = courier_api.api_client.delete(f'/api/v1/courier/{courier_id}')
    # или если есть специальный метод в courier_api:
    # delete_response = courier_api.delete_courier(courier_id)
    
    if delete_response.status_code == 200:
        print(f"Курьер с ID {courier_id} успешно удалён")
    else:
        print(f"Не удалось удалить курьера с ID {courier_id}")