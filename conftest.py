import pytest
from api.base import ApiClient
from api.courier import CourierApi
from api.order import OrderApi


@pytest.fixture
def api_client():
    return ApiClient()


@pytest.fixture
def courier_api(api_client):
    return CourierApi(api_client)


@pytest.fixture
def order_api(api_client):
    return OrderApi(api_client)