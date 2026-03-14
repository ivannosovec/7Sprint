import requests
from constants import BASE_URL


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
            print(f"Error during API POST request to {url}: {e}")
            return response

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)
        return response