import pytest
from datetime import datetime, timedelta
from fastapi import status
from fastapi.testclient import TestClient

from app.api.backend.command import router as command_router
from app.api.backend.order import router as order_router
from app import db

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
def command_api():
    with TestClient(command_router) as client:
        yield client


@pytest.fixture(scope="module")
def order_api():
    with TestClient(order_router) as client:
        yield client


@pytest.fixture(scope="function")
def order_id(order_api):
    response = order_api.post("/", json={})
    if response.status_code != status.HTTP_201_CREATED:
        raise Exception(f"Error en la creación del pedido, código de estado: {response.status_code}")
    order_id: str = response.text
    yield order_id
    response = order_api.delete(f"/{order_id}")
    if response.status_code != status.HTTP_200_OK:
        raise Exception(f"rror en la eliminación del pedido {order_id}, código de estado: {response.status_code}")


def _put_element(command_api: TestClient, order_id: str, element: dict):
    return command_api.put(f"{order_id}/pedido/elements", json=element)


def _get_current_command(command_api: TestClient, order_id: str):
    return command_api.get(f"/{order_id}/pedido")


def _confirm_command(command_api: TestClient, order_id: str):
    return command_api.post(f"{order_id}/pedido/confirmar")


def _close_datetime(d1: datetime, d2: datetime) -> bool:
    return d1 - timedelta(seconds=1) <= d2 <= d1 + timedelta(seconds=1)


@pytest.mark.parametrize("element", [simple_element, complex_element])
def test_get_current_command__when_current_command_exists__then_return_current_command(command_api, order_id, element):
    response = _put_element(command_api, order_id, element)
    assert response.status_code == status.HTTP_200_OK
    response = _get_current_command(command_api, order_id)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [element]


def test_get_current_command__when_order_does_not_exists__then_http_status_404_not_found(command_api):
    response = _get_current_command(command_api, "012345678901234567890123")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_get_current_command__when_current_command_does_not_exists__then_return_empty_list(command_api, order_id):
    response = _get_current_command(command_api, order_id)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


@pytest.mark.parametrize("element", [simple_element, complex_element])
def test_confirm_current_command__when_command_exists__then_return_command(command_api, order_id, element):
    response = _put_element(command_api, order_id, element)
    assert response.status_code == status.HTTP_200_OK
    response = _confirm_command(command_api, order_id)
    assert response.status_code == status.HTTP_200_OK
    assert _close_datetime(response.json()["timestamp"], datetime.now())
    assert response.json()["elements"] == [element]


def test_confirm_current_command__when_order_does_not_exists__then_http_status_404_not_found(command_api):
    response = _confirm_command(command_api, "012345678901234567890123")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_confirm_current_command__when_current_command_does_not_exists__then_http_status_400_bad_request(command_api, order_id):
    response = _confirm_command(command_api, order_id)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.parametrize("element", [simple_element, complex_element])
def test_add_element__when_element_is_correct_and_element_is_new_and_element_quantity_is_grater_than_zero__then_added_to_the_order_and_return_new_element(command_api, order_id, element):
    response = _put_element(command_api, order_id, element)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [element]


@pytest.mark.parametrize("element", [simple_element, complex_element])
def test_add_element__when_element_is_correct_and_element_is_already_exists_and_the_sum_of_both_quantities_is_grater_than_zero__then_element_quantity_is_updated_to_the_sum_of_them_and_return_updated_element(command_api, order_id, element):
    response = _put_element(command_api, order_id, element)
    assert response.status_code == status.HTTP_200_OK
    response = _put_element(command_api, order_id, element)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["quantity"] == element["quantity"] + element["quantity"]
    assert response.json()["clients"] == element["clients"] + element["clients"]


@pytest.mark.parametrize("element, quantity", [
    (simple_element, 0),
    (simple_element, -1),
    (complex_element, 0),
    (complex_element, -1)])
def test_add_element__when_element_is_correct_and_element_is_already_exists_and_the_sum_of_both_quantities_is_less_or_equals_to_zero__then_http_status_400_bad_request(command_api, order_id, element, quantity):
    response = _put_element(command_api, order_id, element)
    assert response.status_code == status.HTTP_200_OK
    over_remove_element = element.copy()
    over_remove_element["quantity"] = element["quantity"] - quantity
    response = _put_element(command_api, order_id, over_remove_element)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.parametrize("element", [simple_element, complex_element])
def test_add_element__when_order_does_not_exists__then_http_status_404_not_found(command_api, element):
    response = _put_element(command_api, "012345678901234567890123", element)
    assert response.status_code == status.HTTP_404_NOT_FOUND


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
    },
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
def test_add_element__when_element_is_not_correct__then_http_status_422_unprocessable_entity(command_api, order_id, element):
    response = _put_element(command_api, order_id, element)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


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
def test_add_element__when_element_does_not_exists__then_http_status_404_not_found(command_api, order_id, element):
    response = _put_element(command_api, order_id, element)
    assert response.status_code == status.HTTP_404_NOT_FOUND
