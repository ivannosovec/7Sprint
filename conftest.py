import pytest
import logging
from api.base import ApiClient
from api.courier import CourierApi
from api.order import OrderApi
from helpers import generate_courier_data

# Настройка логгера для модуля
logger = logging.getLogger(__name__)


@pytest.fixture
def api_client():
    return ApiClient()


@pytest.fixture
def courier_api(api_client):
    return CourierApi(api_client)


@pytest.fixture
def order_api(api_client):
    return OrderApi(api_client)


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
    
    # Логинимся, чтобы получить ID курьера
    login_credentials = {
        "login": courier_data["login"],
        "password": courier_data["password"]
    }
    login_response = courier_api.login_courier(login_credentials)
    assert login_response.status_code == 200, "Не удалось залогиниться"
    courier_id = login_response.json().get("id")
    
    # Возвращаем данные и ID
    yield {"data": courier_data, "id": courier_id}
    
    # После теста удаляем курьера
    delete_response = courier_api.api_client.delete(f'/api/v1/courier/{courier_id}')
    
    # Логируем результат удаления (вместо print)
    if delete_response.status_code == 200:
        logger.info(f"Курьер с ID {courier_id} успешно удалён")
    else:
        logger.error(f"Не удалось удалить курьера с ID {courier_id}")