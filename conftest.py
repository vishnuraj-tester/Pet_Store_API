import pytest
from utils.api_client import APIClient
import random

@pytest.fixture(scope="session")
def api_client():
    return APIClient()

@pytest.fixture
def create_pet_payload():
    pet_id = random.randint(10000, 99999)
    return {
        "id": pet_id,
        "category": {"id": 0, "name": "Dog"},
        "name": "Dobby",
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available"
    }
