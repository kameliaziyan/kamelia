import requests

STATUS_OK = 200
BASE_URL = "http://localhost:8000"

CONNECTION_ERROR = "Cannot connect to server."
OPERATION_FAILED = "Operation failed"


def safe_get(endpoint: str) -> dict | None:
    try:
        response = requests.get(f"{BASE_URL}{endpoint}")
    except requests.exceptions.ConnectionError:
        print(OPERATION_FAILED)
        return None

    if response.status_code != STATUS_OK:
        print(OPERATION_FAILED)
        return None

    return response.json()


def safe_post(endpoint: str, payload: dict) -> dict | None:
    try:
        response = requests.post(
            f"{BASE_URL}{endpoint}",
            json=payload,
        )
    except requests.exceptions.ConnectionError:
        print(CONNECTION_ERROR)
        return None

    if response.status_code != STATUS_OK:
        print(OPERATION_FAILED)
        return None

    return response.json()


def safe_delete(endpoint: str) -> dict | None:
    try:
        response = requests.delete(f"{BASE_URL}{endpoint}")
    except requests.exceptions.ConnectionError:
        print(CONNECTION_ERROR)
        return None

    if response.status_code != STATUS_OK:
        print(OPERATION_FAILED)
        return None

    return response.json()
