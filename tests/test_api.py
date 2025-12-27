import requests

BASE_URL = "http://localhost:8000"

# GET method testing

def test_health():
    req = requests.get(f"{BASE_URL}/health")
    assert req.status_code == 200
    assert req.json() == {"status": "ok"}

def test_valid_request():
    req = requests.get(f"{BASE_URL}/item?id=1")
    assert req.status_code == 200
    assert req.json() == {"id": 1, "name": "Test"}

def test_invalid_request():
    req = requests.get(f"{BASE_URL}/item?id=-1")
    assert req.status_code == 400

def tets_missing_id_param():
    req = requests.get(f"{BASE_URL}/item")
    assert req.status_code == 422

def test_non_int_id():
    req = requests.get(f"{BASE_URL}/item?id=abc")
    assert req.status_code == 422


def test_server_error():
    req = requests.get(f"{BASE_URL}/item?id=10")
    assert req.status_code == 500


# POST method testing

def test_create_item_success():
    payload = {
        "name": "Apple",
        "price": 3.5
    }

    req = requests.post(f"{BASE_URL}/item", json=payload)

    assert req.status_code == 201
    body = req.json()
    assert body["id"] == 1
    assert body["name"] == "Apple"
    assert body["price"] == 3.5

def test_create_item_missing_fields():
    payload = {
        "name": "Apple"
    }

    req = requests.post(f"{BASE_URL}/item", json=payload)

    assert req.status_code == 400
    assert req.json()["detail"] == "Missing required fields"

def test_create_item_invalid_types():
    payload = {
        "name": 123,
        "price": "abc"
    }

    req = requests.post(f"{BASE_URL}/item", json=payload)

    assert req.status_code == 400
    assert req.json()["detail"] == "Invalid field types"