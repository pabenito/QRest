import pytest
from datetime import datetime, timedelta
from fastapi import status
from fastapi.testclient import TestClient
from httpx import Response

from app import app
from app import db

base_url = "/backend/mesa"

db.configure_db(testing=True)

simple_element = {
    "section": "bebidas",
    "element": "nestea",
    "quantity": 1,
    "clients": ["marcos"]
}

complex_element = {
    "section": "pizzas",
    "element": "carbonara",
    "quantity": 3,
    "variants": [
        {
            "name": "tamaño",
            "value": "familiar"
        }
    ],
    "extras": ["albahaca"],
    "ingredients": ["bacon"],
    "clients": ["paula", "marta", "paco"]
}


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


def _put_element(api: TestClient, order_id: str, element: dict):
    return api.put(base_url + f"/{order_id}/pedido/elementos", json=element)


def _get_current_command(api: TestClient, order_id: str):
    return api.get(base_url + f"/{order_id}/pedido")


def _confirm_command(api: TestClient, order_id: str):
    return api.post(base_url + f"/{order_id}/pedido/confirmar")


def _close_datetime(d1: datetime, d2: datetime) -> bool:
    return d1 - timedelta(seconds=1) <= d2 <= d1 + timedelta(seconds=1)


def _print_response(response: Response):
    print(f"\nResponse status code: {response.status_code}\n")
    print(f"\nResponse body: {response.text}\n")


@pytest.mark.parametrize("element", [simple_element, complex_element])
def test_get_current_command__when_current_command_exists__then_http_status_200_ok(api, order_id, element):
    response = _put_element(api, order_id, element)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    response = _get_current_command(api, order_id)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == [element]


def test_get_current_command__when_order_does_not_exists__then_http_status_404_not_found(api):
    response = _get_current_command(api, "012345678901234567890123")
    _print_response(response)
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.text


def test_get_current_command__when_current_command_does_not_exists__then_return_empty_list(api, order_id):
    response = _get_current_command(api, order_id)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == []


@pytest.mark.parametrize("element", [simple_element, complex_element])
def test_confirm_current_command__when_command_exists__then_http_status_200_ok(api, order_id, element):
    response = _put_element(api, order_id, element)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    response = _confirm_command(api, order_id)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text


def test_confirm_current_command__when_order_does_not_exists__then_http_status_404_not_found(api):
    response = _confirm_command(api, "012345678901234567890123")
    _print_response(response)
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.text


def test_confirm_current_command__when_current_command_does_not_exists__then_http_status_404_not_found(api, order_id):
    response = _confirm_command(api, order_id)
    _print_response(response)
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.text


@pytest.mark.parametrize("element", [simple_element, complex_element])
def test_add_element__when_element_is_correct_and_element_is_new_and_element_quantity_is_grater_than_zero__then_added_to_the_order_and_return_new_element(api, order_id, element):
    response = _put_element(api, order_id, element)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == element


@pytest.mark.parametrize("element", [simple_element, complex_element])
def test_add_element__when_element_is_correct_and_element_is_already_exists_and_the_sum_of_both_quantities_is_grater_than_zero__then_element_quantity_is_updated_to_the_sum_of_them_and_return_updated_element(api, order_id, element):
    response = _put_element(api, order_id, element)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    response = _put_element(api, order_id, element)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json()["quantity"] == element["quantity"] + element["quantity"]
    assert response.json()["clients"] == element["clients"] + element["clients"]


@pytest.mark.parametrize("element, quantity", [
    (simple_element, -1),
    (complex_element, -1)])
def test_add_element__when_element_is_correct_and_element_is_already_exists_and_the_sum_of_both_quantities_is_less_than_zero__then_http_status_400_bad_request(api, order_id, element, quantity):
    response = _put_element(api, order_id, element)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    over_remove_element = element.copy()
    over_remove_element["quantity"] = element["quantity"] - quantity
    response = _put_element(api, order_id, over_remove_element)
    _print_response(response)
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.text


@pytest.mark.parametrize("element", [simple_element, complex_element])
def test_add_element__when_order_does_not_exists__then_http_status_404_not_found(api, element):
    response = _put_element(api, "012345678901234567890123", element)
    _print_response(response)
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.text


@pytest.mark.parametrize("element", [
    {},
    {
        "element": "nestea",
        "quantity": 1,
        "clients": ["marcos"]
    },
    {
        "section": "bebidas",
        "quantity": 1,
        "clients": ["marcos"]
    },
    {
        "section": "bebidas",
        "element": "nestea",
        "clients": ["marcos"]
    },
    {
        "section": "bebidas",
        "element": "nestea",
        "quantity": 1,
        "clients": []
    }
])
def test_add_element__when_element_is_not_correct__then_http_status_422_unprocessable_entity(api, order_id, element):
    response = _put_element(api, order_id, element)
    _print_response(response)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.text


@pytest.mark.parametrize("element", [
    {
        "section": "seccion que no existe",
        "element": "nestea",
        "quantity": 1,
        "clients": ["marcos"]
    },
    {
        "section": "bebidas",
        "element": "elemento que no existe",
        "quantity": 1,
        "clients": ["marcos"]
    },
])
def test_add_element__when_element_does_not_exists__then_http_status_404_not_found(api, order_id, element):
    response = _put_element(api, order_id, element)
    _print_response(response)
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.text
