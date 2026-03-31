import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def get_response(base_url):
    def _get(endpoint):
        response = requests.get(base_url + endpoint)
        return response
    return _get