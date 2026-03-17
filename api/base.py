import requests
import logging
from constants import BASE_URL

# Настройка логгера для модуля
logger = logging.getLogger(__name__)


class ApiClient:
    def __init__(self):
        self.base_url = BASE_URL

    def post(self, endpoint, data=None):
        url = f'{self.base_url}{endpoint}'
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            response = e.response
            # Заменяем print на логирование
            logger.error(f"API POST request to {url} failed: {e}")
            return response

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)
        return response