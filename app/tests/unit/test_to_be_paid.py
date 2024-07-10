from copy import deepcopy
from pprint import pprint

import pytest
from fastapi import status
from fastapi.testclient import TestClient
from httpx import Response

from app import app
from app import db

base_url = "/backend/mesa"

simple_element1 = {
    "section": "bebidas",
    "element": "nestea",
    "quantity": 1,
    "clients": ["marcos"],
    "price": 2,
    "total": 2
}

simple_element2 = {
    "section": "bebidas",
    "element": "coca-cola",
    "quantity": 1,
    "clients": ["lola"],
    "price": 2,
    "total": 2
}


def generate_receipt(list_elements: list[dict]) -> list[dict]:
    receipt = {}
    for element in list_elements:
        if element["element"] in receipt:
            receipt[element["element"]]["quantity"] += element["quantity"]
            receipt[element["element"]]["clients"].extend(element["clients"])
            receipt[element["element"]]["total"] += element["price"] * element["quantity"]
        else:
            receipt[element["element"]] = deepcopy(element)
            receipt[element["element"]]["price"] = element["price"]
            receipt[element["element"]]["total"] = element["price"] * element["quantity"]
    return list(receipt.values())

def get_receipt_for_client(list_elements: list[dict], client: str) -> list[dict]:
    receipt = {}
    for element in list_elements:
        if client in element["clients"]:
            if element["element"] in receipt:
                receipt[element["element"]]["quantity"] += element["clients"].count(client)
                receipt[element["element"]]["clients"].extend([client] * element["clients"].count(client))
                receipt[element["element"]]["total"] += element["price"] * element["clients"].count(client)
            else:
                receipt[element["element"]] = deepcopy(element)
                receipt[element["element"]]["quantity"] = element["clients"].count(client)
                receipt[element["element"]]["clients"] = [client] * element["clients"].count(client)
                receipt[element["element"]]["price"] = element["price"]
                receipt[element["element"]]["total"] = element["price"] * element["clients"].count(client)
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
    return api.post(base_url + f"/{order_id}/recibo")


def _get_to_be_paid(api: TestClient, order_id: str):
    return api.get(base_url + f"/{order_id}/por_pagar")


def _get_to_be_paid_client(api: TestClient, order_id: str, client: str):
    return api.get(base_url + f"/{order_id}/por_pagar?client={client}")


def _pay(api: TestClient, order_id: str, elements: list[dict]):
    return api.post(base_url + f"/{order_id}/pagar", json=elements)


def _print_response(response: Response):
    print(f"\nResponse status code: {response.status_code}\n")
    print(f"Response body: {response.text}\n")


@pytest.mark.parametrize("elements", [
    [simple_element1, simple_element2],
    [simple_element1, simple_element1],
    [simple_element2, simple_element2]])
def test_get_to_be_paid_total__when_order_exists_and_one_confirmed_order_exists_and_receipt_exists__then_return_total_receipt_http_status_200_ok(api, order_id, elements: list[dict]):
    for element in elements:
        response = _put_element(api, order_id, element)
        _print_response(response)
        assert response.status_code == status.HTTP_200_OK, response.text
    response = _confirm_command(api, order_id)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    response = _generate_receipt(api, order_id)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    response = _get_to_be_paid(api, order_id)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == generate_receipt(elements)


@pytest.mark.parametrize("elements", [
    [simple_element1, simple_element2],
    [simple_element1, simple_element1],
    [simple_element2, simple_element2]])
def test_get_to_be_paid_total__when_order_exists_and_one_confirmed_order_exists_and_receipt_exists_and_something_have_been_paid__then_return_receipt_less_already_paid_http_status_200_ok(api, order_id, elements: list[dict]):
    for element in elements:
        response = _put_element(api, order_id, element)
        _print_response(response)
        assert response.status_code == status.HTTP_200_OK, response.text
    response = _confirm_command(api, order_id)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    response = _generate_receipt(api, order_id)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    pprint(response.json()[0])
    response = _pay(api, order_id, [response.json()[0]])
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    response = _get_to_be_paid(api, order_id)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == generate_receipt(elements[1:len(elements)])


@pytest.mark.parametrize("elements", [
    [simple_element1, simple_element2],
    [simple_element1, simple_element1],
    [simple_element2, simple_element2]])
def test_get_to_be_paid_client__when_order_exists_and_one_confirmed_order_exists_and_receipt_exists__then_return_client_receipt_and_http_status_200_ok(api, order_id, elements: list[dict]):
    for element in elements:
        response = _put_element(api, order_id, element)
        _print_response(response)
        assert response.status_code == status.HTTP_200_OK, response.text
    response = _confirm_command(api, order_id)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    response = _generate_receipt(api, order_id)
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    response = _get_to_be_paid_client(api, order_id, elements[0]["clients"][0])
    _print_response(response)
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == get_receipt_for_client(elements, elements[0]["clients"][0])

def test_get_to_be_paid_total__when_order_does_not_exists__then_http_status_404_not_found(api):
    response = _get_to_be_paid(api, "012345678901234567890123")
    _print_response(response)
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.text

def test_get_to_be_paid_client__when_order_does_not_exists__then_http_status_404_not_found(api):
    response = _get_to_be_paid_client(api, "012345678901234567890123", "marcos")
    _print_response(response)
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.text

def test_get_to_be_paid_total__when_order_exists_and_no_receipt_exists__then_http_status_400_bad_request(api, order_id):
    response = _get_to_be_paid(api, order_id)
    _print_response(response)
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.text

def test_get_to_be_paid_client__when_order_exists_and_no_receipt_exists__then_http_status_400_bad_request(api, order_id):
    response = _get_to_be_paid_client(api, order_id, "marcos")
    _print_response(response)
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.text

