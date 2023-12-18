import pytest
from fastapi import status
from fastapi.testclient import TestClient
from httpx import Response

from app import app
from app import db

base_url = "/backend/mesa"

simple_element = {
    "section": "bebidas",
    "element": "nestea",
    "quantity": 1,
    "clients": ["marcos"],
    "price": 2
}

simple_element_receipt = {
    "section": "bebidas",
    "element": "nestea",
    "quantity": 1,
    "clients": ["marcos"],
    "price": 2,
}


def generate_receipt(list_elements: list[dict]) -> list[dict]:
    receipt = {}
    for element in list_elements:
        if element["element"] in receipt:
            receipt[element["element"]]["quantity"] += element["quantity"]
            receipt[element["element"]]["clients"].extend(element["clients"])
            receipt[element["element"]]["total"] += element["price"] * element["quantity"]
        else:
            receipt[element["element"]] = element
            receipt[element["element"]]["total"] = element["price"] * element["quantity"]
    return list(receipt.values())


@pytest.fixture(scope="module")
def api():
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="function")
def order_id(api):
    response = api.post(base_url + "/", json={})
    if response.status_code != status.HTTP_201_CREATED:
        raise Exception(f"Error en la creación del pedido, código de estado: {response.status_code}")
    order_id: str = response.text.replace('"', '')
    yield order_id
    response = api.delete(base_url + f"/{order_id}")
    if response.status_code != status.HTTP_200_OK:
        raise Exception(f"rror en la eliminación del pedido {order_id}, código de estado: {response.status_code}")


def setup_function(function):
    db.configure_db(testing=True)


def _put_element(api: TestClient, order_id: str, element: dict):
    return api.put(base_url + f"/{order_id}/pedido/elementos", json=element)


def _get_current_command(api: TestClient, order_id: str):
    return api.get(base_url + f"/{order_id}/pedido")


def _confirm_command(api: TestClient, order_id: str):
    return api.post(base_url + f"/{order_id}/pedido/confirmar")


def _generate_receipt(api: TestClient, order_id: str):
    return api.post(base_url + f"/{order_id}/pedido/recibo")


def _print_response(response: Response):
    print(f"\nResponse status code: {response.status_code}\n")
    print(f"\nResponse body: {response.text}\n")


@pytest.mark.parametrize("element", [simple_element])
def test_post_generate_receipt__when_order_exists_and_one_confirmed_order_exists__then_http_status_200_ok(api, order_id, element: dict):
    response = _put_element(api, order_id, element)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    response = _confirm_command(api, order_id)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == [element]
    response = _generate_receipt(api, order_id)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == generate_receipt([simple_element_receipt])

@pytest.mark.parametrize("element", [simple_element])
def test_post_generate_receipt__when_order_exists_and_two_confirmed_order_exists__then_http_status_200_ok(api, order_id, element: dict):
    response = _put_element(api, order_id, element)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    response = _confirm_command(api, order_id)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == [element]
    _put_element(api, order_id, element)
    _confirm_command(api, order_id)
    response = _generate_receipt(api, order_id)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == generate_receipt([simple_element_receipt, simple_element_receipt])

def test_post_generate_receipt__when_order_does_not_exists__then_http_status_404_not_found(api):
    response = _generate_receipt(api, "012345678901234567890123")
    _print_response(response)
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.text

def test_post_generate_receipt__when_order_exists_and_no_confirmed_order_exists__then_http_status_400_bad_request(api, order_id):
    response = _put_element(api, order_id, simple_element)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    response = _generate_receipt(api, order_id)
    _print_response(response)
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.text
    _print_response(response)
