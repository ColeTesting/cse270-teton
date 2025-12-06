import pytest
import responses
import requests

BASE_URL = "http://127.0.0.1:8000/users/"


@responses.activate
def test_user_endpoint_valid_credentials_mocked():
    """
    Test 1: Mock the endpoint with valid credentials.
    Expect HTTP 200 and empty response body.
    """
    # Mocked URL with expected query parameters
    responses.add(
        responses.GET,
        BASE_URL,
        match=[responses.matchers.query_param_matcher({
            "username": "admin",
            "password": "qwerty"
        })],
        status=200,
        body=""
    )

    params = {"username": "admin", "password": "qwerty"}
    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 200
    assert response.text.strip() == ""


@responses.activate
def test_user_endpoint_invalid_credentials_mocked():
    """
    Test 2: Mock the endpoint with invalid credentials.
    Expect HTTP 401 and empty response body.
    """
    responses.add(
        responses.GET,
        BASE_URL,
        match=[responses.matchers.query_param_matcher({
            "username": "admin",
            "password": "admin"
        })],
        status=401,
        body=""
    )

    params = {"username": "admin", "password": "admin"}
    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 401
    assert response.text.strip() == ""
