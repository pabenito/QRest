from pprint import pprint

import pytest
from fastapi import status
from fastapi.testclient import TestClient
from fastapi.exceptions import RequestValidationError, HTTPException
from bson import ObjectId
from app.utils import json_lower_encoder
from .menu import router, menu, check_price
from .models import Element, Variants, Variant

client = TestClient(router)


# Check price

def test___check_price___when_price_is_set_and_there_is_not_variants___then_dont_raise_exception():
    element = Element(name="Nestea", manager="Waiter")
    element.price = 2.5
    check_price(element)


def test___check_price___when_price_is_set_and_there_is_at_least_a_variant_with_price___then_raise_exception():
    element = Element(name="Agua", manager="Waiter")
    element.price = 1
    element.variants = [Variants(name="Tamaño", variants=[Variant(description="grande", price=2)])]

    with pytest.raises(AttributeError):
        check_price(element)


def test___check_price___when_price_is_not_set_and_there_is_not_variants___then_raise_exception():
    element = Element(name="Agua", manager="Waiter")

    with pytest.raises(AttributeError):
        check_price(element)


def test___check_price___when_price_is_not_set_and_all_variants_have_price___then_dont_raise_exception():
    element = Element(name="Agua", manager="Waiter")
    element.variants = [Variants(name="Tamaño", variants=[
        Variant(description="pequeña", price=1),
        Variant(description="grande", price=2)])]
    check_price(element)


# Seccion

## Post

def test_carta_post___when_correct___creates_seccion():
    try:
        response = client.post("/", json=section_example)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == section_example
    finally:
        client.delete("/" + section_example["name"])



def test_carta_post___when_insert_seccion_with_same_name___raises_exception():
    client.post("/", json=section_example)
    with pytest.raises(HTTPException) as err:
        client.post("/", json=section_example)
    assert err.value.status_code == status.HTTP_409_CONFLICT
    client.delete("/" + section_example["name"])



def test_carta_post___when_not_requiered_field___raises_exception():
    post = {"visible": False}
    with pytest.raises(RequestValidationError):
        client.post("/", json=post)


## Get

def test_carta_get___when_post___then_get_has_one_more_document():
    try:
        count_before = menu.count_documents({})
        client.post("/", json=section_example)
        assert menu.count_documents({}) == count_before + 1
    finally:
        client.delete("/" + section_example["name"])



def test_carta_get___when_post___then_can_get_seccion():
    try:
        client.post("/", json=section_example)
        response = client.get("/" + section_example["name"])
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == section_example
    finally:
        client.delete("/" + section_example["name"])



def test_carta_get___when_get_with_invalid_seccion_name___then_raises_exception():
    with pytest.raises(HTTPException) as err:
        client.get("/not_a_seccion")
    assert err.value.status_code == status.HTTP_404_NOT_FOUND


## Delete

def test_carta_delete___when_section_exists___delete_seccion():
    response = client.post("/", json=section_example)
    response = client.delete("/" + section_example["name"])
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == section_example



def test_carta_delete___when_delete_with_invalid_seccion_name___then_raises_exception():
    with pytest.raises(HTTPException) as err:
        client.delete("/not_a_seccion")
    assert err.value.status_code == status.HTTP_404_NOT_FOUND


## Put

def test_carta_put___when_put_with_invalid_seccion_name___then_raises_exception():
    with pytest.raises(HTTPException) as err:
        client.put("/not_a_seccion", json={"name": "x"})
    assert err.value.status_code == status.HTTP_404_NOT_FOUND



def test_carta_put___when_put_another_name___then_replaces_name():
    try:
        new_name = "new_name"
        post_correct_output_with_new_name = section_example.copy()
        post_correct_output_with_new_name["name"] = new_name
        client.post("/", json=section_example)
        id = client.get("/" + section_example["name"] + "/id").json()["_id"]
        response = client.put("/" + section_example["name"], json={"name": new_name})
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == post_correct_output_with_new_name
    finally:
        menu.delete_one({"_id": ObjectId(id)})


# Elements

## Post

def test_elements_post___when_correct___then_add_element():
    try:
        section = base_section.copy()
        client.post("/", json=section.copy())
        section["elements"] = [element_example]
        response = client.post("/" + section["name"], json=element_example.copy())
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == section
    finally:
        client.delete("/" + base_section["name"])


## Put

def test_elements_put___when_correct___then_update_element():
    try:
        section = base_section.copy()
        section["elements"] = [element_example.copy()]
        client.post("/", json=section.copy())
        section["elements"][0]["manager"] = "test_responsable"
        response = client.put(f"/{section['name']}/{section['elements'][0]['name']}", json=section["elements"][0])
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == json_lower_encoder(section)
    finally:
        client.delete("/" + section["name"])



def test_elements_put___when_set_another_name___then_rename_element():
    try:
        section = base_section.copy()
        section["elements"] = [element_example.copy()]
        client.post("/", json=section.copy())
        old_name = section["elements"][0]["name"]
        section["elements"][0]["name"] = "new_name"
        response = client.put(f"/{section['name']}/{old_name}", json=section["elements"][0])
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == json_lower_encoder(section)
    finally:
        client.delete("/" + section["name"])



def test_elements_put___when_set_another_name_that_exists___then_raise_exception():
    try:
        section = base_section.copy()
        an_element = element_example.copy()
        other_element = element_example.copy()
        other_element["name"] = "other_name"
        section["elements"] = [an_element, other_element]
        client.post("/", json=section)
        an_element_with_other_name = an_element.copy()
        an_element_with_other_name["name"] = other_element["name"]
        with pytest.raises(HTTPException) as err:
            client.put(f"/{section['name']}/{an_element['name']}", json=an_element_with_other_name)
        assert err.value.status_code == status.HTTP_409_CONFLICT
    finally:
        client.delete("/" + section["name"])



def test_elements_put___when_section_dont_exists___then_raise_exception():
    with pytest.raises(HTTPException) as err:
        client.put("/not_a_seccion/not_an_element", json=element_example.copy())
    assert err.value.status_code == status.HTTP_404_NOT_FOUND



def test_elements_put___when_element_dont_exists_in_section___then_raise_exception():
    try:
        section = base_section.copy()
        section["elements"] = [element_example.copy()]
        client.post("/", json=section)
        with pytest.raises(HTTPException) as err:
            client.put(f"/{section['name']}/not_an_element", json=element_example.copy())
        assert err.value.status_code == status.HTTP_404_NOT_FOUND
    finally:
        client.delete("/" + section["name"])


## Delete

def test_elements_delete___when_element_exists___then_delete_it():
    try:
        section = base_section.copy()
        section["elements"] = [element_example.copy()]
        client.post("/", json=section.copy())
        respose = client.delete(f"/{section['name']}/{section['elements'][0]['name']}")
        assert respose.status_code == status.HTTP_200_OK
        print(respose.json())
        print(section)
        assert respose.json() == section
    finally:
        client.delete(f"/{section['name']}")



def test_elements_delete___when_element_dont_exists___then_raise_exception():
    try:
        client.post("/", json=base_section.copy())
        with pytest.raises(HTTPException) as err:
            client.delete(f"/{base_section['name']}/not_an_element")
        assert err.value.status_code == status.HTTP_404_NOT_FOUND
    finally:
        client.delete(f"/{base_section['name']}")


base_section = {"name": "test_base_section"}

section_example = {
    "name": "bebidas",
    "elements": [
        {
            "name": "agua",
            "image": "https://image.com/image.jpg",
            "manager": "camareros",
            "variants": [
                {
                    "name": "tamaño",
                    "variants": [
                        {
                            "description": "500ml",
                            "price": 1
                        },
                        {
                            "description": "1,5l",
                            "price": 2
                        }
                    ]
                }
            ]
        },
        {
            "name": "limonada",
            "image": "https://image.com/image.jpg",
            "description": "limonada de la casa",
            "price": 3,
            "manager": "camareros",
            "ingredients": [
                "limón",
                "azúzar"
            ],
            "extras": [
                {
                    "description": "hiebabuena",
                    "price": 1
                }
            ]
        }
    ]
}

element_example = {
    "name": "coca-cola",
    "price": 2.5,
    "manager": "camareros",
    "variants": [
        {
            "name": "tipo",
            "variants": [
                {
                    "description": "normal"
                },
                {
                    "description": "zero"
                },
                {
                    "description": "zero zero"
                }
            ]
        }
    ]
}
