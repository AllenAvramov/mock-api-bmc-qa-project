import requests

BASE_URL = "http://localhost:8000"

def test_valid_request():
    req = requests.get(f"{BASE_URL}/item?id=1")
    assert req.status_code == 200

def test_invalid_request():
    req = requests.get(f"{BASE_URL}/item?id=-1")
    assert req.status_code == 400

def test_server_error():
    req = requests.get(f"{BASE_URL}/item?id=10")
    assert req.status_code == 500