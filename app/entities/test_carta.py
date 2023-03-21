from pprint import pprint

import pytest
from fastapi import status
from fastapi.testclient import TestClient
from fastapi.exceptions import RequestValidationError, HTTPException
from bson import ObjectId
from app.utils import json_lower_encoder
from .carta import router, carta, check_precio
from .models import Elemento_carta, Variantes, Variante

client = TestClient(router)


# Check precio

def test___check_precio___when_precio_is_set_and_there_is_not_variantes___then_dont_raise_exception():
    elemento = Elemento_carta(nombre="Nestea")
    elemento.precio = 2.5
    check_precio(elemento)


def test___check_precio___when_precio_is_set_and_there_is_at_least_a_variante_with_price___then_raise_exception():
    elemento = Elemento_carta(nombre="Agua")
    elemento.precio = 1
    elemento.variantes = [Variantes(nombre="Tamaño", variantes=[Variante(descripcion="grande", precio=2)])]

    with pytest.raises(AttributeError):
        check_precio(elemento)


def test___check_precio___when_precio_is_not_set_and_there_is_not_variantes___then_raise_exception():
    elemento = Elemento_carta(nombre="Agua")

    with pytest.raises(AttributeError):
        check_precio(elemento)


def test___check_precio___when_precio_is_not_set_and_all_variantes_have_price___then_dont_raise_exception():
    elemento = Elemento_carta(nombre="Agua")
    elemento.variantes = [Variantes(nombre="Tamaño", variantes=[
        Variante(descripcion="pequeña", precio=1),
        Variante(descripcion="grande", precio=2)])]
    check_precio(elemento)


# Seccion

## Post

def test_carta_post___when_correct___creates_seccion():
    try:
        response = client.post("/", json=post_correct_section_input)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == post_correct_section_output
    finally:
        client.delete("/" + post_correct_section_input["nombre"])


def test_carta_post___when_insert_seccion_with_same_nombre___raises_exception():
    client.post("/", json=post_correct_section_input)
    with pytest.raises(HTTPException) as err:
        client.post("/", json=post_correct_section_input)
    assert err.value.status_code == status.HTTP_409_CONFLICT
    client.delete("/" + post_correct_section_input["nombre"])


def test_carta_post___when_not_requiered_field___raises_exception():
    post = {"visible": False}
    with pytest.raises(RequestValidationError):
        client.post("/", json=post)


## Get

def test_carta_get___when_post___then_get_has_one_more_document():
    try:
        count_before = carta.count_documents({})
        client.post("/", json=post_correct_section_input)
        assert carta.count_documents({}) == count_before + 1
    finally:
        client.delete("/" + post_correct_section_input["nombre"])


def test_carta_get___when_post___then_can_get_seccion():
    try:
        client.post("/", json=post_correct_section_input)
        response = client.get("/" + post_correct_section_input["nombre"])
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == post_correct_section_output
    finally:
        client.delete("/" + post_correct_section_input["nombre"])


def test_carta_get___when_get_with_invalid_seccion_nombre___then_raises_exception():
    with pytest.raises(HTTPException) as err:
        client.get("/not_a_seccion")
    assert err.value.status_code == status.HTTP_404_NOT_FOUND


## Delete

def test_carta_delete___when_section_exists___delete_seccion():
    response = client.post("/", json=post_correct_section_input)
    response = client.delete("/" + post_correct_section_input["nombre"])
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == post_correct_section_output


def test_carta_delete___when_delete_with_invalid_seccion_nombre___then_raises_exception():
    with pytest.raises(HTTPException) as err:
        client.delete("/not_a_seccion")
    assert err.value.status_code == status.HTTP_404_NOT_FOUND


## Put

def test_carta_put___when_put_with_invalid_seccion_nombre___then_raises_exception():
    with pytest.raises(HTTPException) as err:
        client.put("/not_a_seccion", json={"nombre": "x"})
    assert err.value.status_code == status.HTTP_404_NOT_FOUND


def test_carta_put___when_put_another_nombre___then_replaces_nombre():
    try:
        new_nombre = "new_nombre"
        post_correct_output_with_new_name = post_correct_section_output.copy()
        post_correct_output_with_new_name["nombre"] = new_nombre
        client.post("/", json=post_correct_section_input)
        id = client.get("/" + post_correct_section_input["nombre"] + "/id").json()["_id"]
        response = client.put("/" + post_correct_section_input["nombre"], json={"nombre": new_nombre})
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == post_correct_output_with_new_name
    finally:
        carta.delete_one({"_id": ObjectId(id)})


# Elements

## Post

def test_elements_post___when_correct___then_add_element():
    try:
        client.post("/", json=base_section.copy())
        response = client.post("/" + base_section["nombre"], json=post_correct_element_input.copy())
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == post_correct_element_in_section_output
    finally:
        client.delete("/" + base_section["nombre"])


## Put

def test_elements_put___when_correct___then_update_element():
    try:
        section = base_section.copy()
        section["elementos"] = [post_correct_element_output.copy()]
        client.post("/", json=section.copy())
        section["elementos"][0]["responsable"] = "test_responsable"
        response = client.put(f"/{section['nombre']}/{section['elementos'][0]['nombre']}", json=section["elementos"][0])
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == json_lower_encoder(section)
    finally:
        client.delete("/" + section["nombre"])


def test_elements_put___when_set_another_name___then_rename_element():
    try:
        section = base_section.copy()
        section["elementos"] = [post_correct_element_output.copy()]
        client.post("/", json=section.copy())
        old_name = section["elementos"][0]["nombre"]
        section["elementos"][0]["nombre"] = "new_name"
        response = client.put(f"/{section['nombre']}/{old_name}", json=section["elementos"][0])
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == json_lower_encoder(section)
    finally:
        client.delete("/" + section["nombre"])


def test_elements_put___when_set_another_name_that_exists___then_raise_exception():
    try:
        section = base_section.copy()
        an_element = post_correct_element_output.copy()
        other_element = post_correct_element_output.copy()
        other_element["nombre"] = "other_name"
        section["elementos"] = [an_element, other_element]
        client.post("/", json=section)
        an_element_with_other_name = an_element.copy()
        an_element_with_other_name["nombre"] = other_element["nombre"]
        with pytest.raises(HTTPException) as err:
            client.put(f"/{section['nombre']}/{an_element['nombre']}", json=an_element_with_other_name)
        assert err.value.status_code == status.HTTP_409_CONFLICT
    finally:
        client.delete("/" + section["nombre"])


def test_elements_put___when_section_dont_exists___then_raise_exception():
    with pytest.raises(HTTPException) as err:
        client.put("/not_a_seccion/not_an_element", json=post_correct_element_input.copy())
    assert err.value.status_code == status.HTTP_404_NOT_FOUND


def test_elements_put___when_element_dont_exists_in_section___then_raise_exception():
    try:
        section = base_section.copy()
        section["elementos"] = [post_correct_element_output.copy()]
        client.post("/", json=section)
        with pytest.raises(HTTPException) as err:
            client.put(f"/{section['nombre']}/not_an_element", json=post_correct_element_output.copy())
        assert err.value.status_code == status.HTTP_404_NOT_FOUND
    finally:
        client.delete("/" + section["nombre"])


## Delete

def test_elements_delete___when_element_exists___then_delete_it():
    try:
        section = base_section.copy()
        section["elementos"] = [post_correct_element_output.copy()]
        client.post("/", json=section.copy())
        respose = client.delete(f"/{section['nombre']}/{section['elementos'][0]['nombre']}")
        assert respose.status_code == status.HTTP_200_OK
        assert respose.json() == section
    finally:
        client.delete(f"/{section['nombre']}")


def test_elements_delete___when_element_dont_exists___then_raise_exception():
    try:
        client.post("/", json=base_section.copy())
        with pytest.raises(HTTPException) as err:
            client.delete(f"/{base_section['nombre']}/not_an_element")
        assert err.value.status_code == status.HTTP_404_NOT_FOUND
    finally:
        client.delete(f"/{base_section['nombre']}")


base_section = {"nombre": "test_base_section"}

post_correct_section_input = {
    "nombre": "test_bebidas",
    "visible": True,
    "elementos": [
        {
            "nombre": "agua",
            "imagen": "https://image.freepik.com/foto-gratis/agua-fria-botella-plastico-tapa-azul-colocada-pasarela-cemento_33789-101.jpg",
            "responsable": "camareros",
            "visible": True,
            "variantes": [
                {
                    "nombre": "tamaño",
                    "variantes": [
                        {
                            "descripcion": "500mL",
                            "precio": 1
                        },
                        {
                            "descripcion": "1,5L",
                            "precio": 2
                        }
                    ]
                }
            ]
        },
        {
            "nombre": "limonada",
            "imagen": "https://www.pequerecetas.com/wp-content/uploads/2021/05/limonada-como-se-hace.jpg",
            "descripcion": "limonada de la casa",
            "precio": 3,
            "responsable": "camareros",
            "visible": True,
            "ingredientes": [
                "limón",
                "azúzar"
            ],
            "extras": [
                {
                    "descripcion": "hiebabuena",
                    "precio": 1
                }
            ]
        }
    ]
}

post_correct_section_output = {
    "nombre": "test_bebidas",
    "elementos": [
        {
            "nombre": "agua",
            "imagen": "https://image.freepik.com/foto-gratis/agua-fria-botella-plastico-tapa-azul-colocada-pasarela-cemento_33789-101.jpg",
            "responsable": "camareros",
            "variantes": [
                {
                    "nombre": "tamaño",
                    "variantes": [
                        {
                            "descripcion": "500ml",
                            "precio": 1
                        },
                        {
                            "descripcion": "1,5l",
                            "precio": 2
                        }
                    ]
                }
            ]
        },
        {
            "nombre": "limonada",
            "imagen": "https://www.pequerecetas.com/wp-content/uploads/2021/05/limonada-como-se-hace.jpg",
            "descripcion": "limonada de la casa",
            "precio": 3,
            "responsable": "camareros",
            "ingredientes": [
                "limón",
                "azúzar"
            ],
            "extras": [
                {
                    "descripcion": "hiebabuena",
                    "precio": 1
                }
            ]
        }
    ]
}

post_correct_element_input = {
    "nombre": "Coca-cola",
    "precio": 2.5,
    "responsable": "camareros",
    "visible": True,
    "variantes": [
        {
            "nombre": "Tipo",
            "variantes": [
                {
                    "descripcion": "normal"
                },
                {
                    "descripcion": "Zero"
                },
                {
                    "descripcion": "Zero Zero"
                }
            ]
        }
    ]
}

post_correct_element_output = {
    "nombre": "coca-cola",
    "precio": 2.5,
    "responsable": "camareros",
    "variantes": [
        {
            "nombre": "tipo",
            "variantes": [
                {
                    "descripcion": "normal"
                },
                {
                    "descripcion": "zero"
                },
                {
                    "descripcion": "zero zero"
                }
            ]
        }
    ]
}

post_correct_element_in_section_output = base_section.copy()
post_correct_element_in_section_output["elementos"] = [post_correct_element_output]
