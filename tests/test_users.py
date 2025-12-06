import requests
import pytest

BASE_URL = "http://127.0.0.1:8000/users/"


def test_user_endpoint_valid_credentials(requests_mock):
    """
    Test 1: Mock the endpoint with valid credentials.
    Expect HTTP 200 and empty response body.
    """
    # Build the exact URL with query params
    url = f"{BASE_URL}?username=admin&password=qwerty"

    # Mock the GET request
    requests_mock.get(url, status_code=200, text="")

    # Execute the request
    response = requests.get(BASE_URL, params={"username": "admin", "password": "qwerty"})

    assert response.status_code == 200
    assert response.text.strip() == ""


def test_user_endpoint_invalid_credentials(requests_mock):
    """
    Test 2: Mock the endpoint with invalid credentials.
    Expect HTTP 401 and empty response body.
    """
    url = f"{BASE_URL}?username=admin&password=admin"

    requests_mock.get(url, status_code=401, text="")

    response = requests.get(BASE_URL, params={"username": "admin", "password": "admin"})

    assert response.status_code == 401
    assert response.text.strip() == ""
