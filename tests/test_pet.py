import pytest

def test_add_and_get_pet(api_client, create_pet_payload):
    response = api_client.send_request("POST", "/pet", create_pet_payload)
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "Dobby"

    pet_id = data["id"]

    response = api_client.send_request("GET", f"/pet/{pet_id}")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == pet_id

def test_get_invalid_pet(api_client):
    response = api_client.send_request("GET", "/pet/99999999999999")
    assert response.status_code in [404, 400]

def test_delete_pet(api_client, create_pet_payload):
    response = api_client.send_request("POST", "/pet", create_pet_payload)
    pet_id = response.json()["id"]

    response = api_client.send_request("DELETE", f"/pet/{pet_id}")
    assert response.status_code == 200

