# Import libraries
from pprint import pprint

from fastapi import APIRouter, status, HTTPException
from app.entities.models import Seccion, Elemento_carta
from app.database import db
from app.utils import json_lower_encoder

# Create router
router = APIRouter()

# Collections
carta = db["carta"]


# Seccion
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Seccion, response_model_exclude_unset=True)
def create_seccion(seccion: Seccion):
    if carta.find_one({"nombre": seccion.nombre}) is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"La sección '{seccion.nombre}', ya existe.")

    if seccion.elementos is not None:
        for elemento in seccion.elementos:
            check_precio(elemento)

    seccion = json_lower_encoder(seccion)
    new_seccion = carta.insert_one(seccion)
    created_seccion = carta.find_one({"_id": new_seccion.inserted_id})

    return created_seccion


@router.get("/", response_model=list[Seccion], response_model_exclude_unset=True)
def get_carta():
    return list(carta.find({}))


@router.get("/{seccion}", response_model=Seccion, response_model_exclude_unset=True)
def get_seccion(seccion: str):
    return get_section(seccion)


@router.get("/{seccion}/id")
def get_seccion_id(seccion: str):
    seccion_id = carta.find_one({"nombre": seccion}, {"_id": True})
    if seccion_id is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La sección '{seccion}', no existe.")
    return {"_id": str(seccion_id["_id"])}


@router.put("/{seccion}", response_model=Seccion, response_model_exclude_unset=True)
def update_seccion(seccion: str, seccion_body: Seccion):
    old_seccion_json = carta.find_one({"nombre": seccion.lower()})
    if old_seccion_json is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La sección '{seccion}', no existe.")
    old_seccion = Seccion.parse_obj(old_seccion_json)

    if seccion_body.nombre.lower() != old_seccion.nombre and carta.count_documents(
            {"nombre": seccion_body.nombre.lower()}) > 0:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"La sección '{seccion.nombre}', ya existe.")

    if seccion_body.elementos is not None:
        for elemento in seccion.elementos:
            check_precio(elemento)

    new_seccion = json_lower_encoder(seccion_body)
    updated_secction = old_seccion.copy(update=new_seccion)
    carta.find_one_and_update(
        {"nombre": seccion.lower()},
        {"$set": json_lower_encoder(updated_secction)})

    return carta.find_one({"_id": old_seccion_json["_id"]})


@router.delete("/{seccion}", response_model=Seccion, response_model_exclude_unset=True)
def delete_seccion(seccion: str):
    section = get_section(seccion)
    carta.delete_one({"nombre": seccion.lower()})
    return section


# Elementos
@router.post("/{seccion}", response_model=Seccion, response_model_exclude_unset=True)
def add_elemento_seccion(seccion: str, elemento: Elemento_carta):
    check_section_exists(seccion)
    check_precio(elemento)
    carta.find_one_and_update({"nombre": seccion.lower()}, {"$push": {"elementos": json_lower_encoder(elemento)}})
    return carta.find_one({"nombre": seccion})


@router.put("/{seccion}/{elemento}", response_model=Seccion, response_model_exclude_unset=True)
def update_elemento_seccion(seccion: str, elemento: str, elemento_body: Elemento_carta):
    check_section_exists(seccion)
    check_element_exists(seccion, elemento)
    check_precio(elemento_body)

    if elemento.lower() != elemento_body.nombre.lower() \
            and carta.count_documents(
        {"nombre": seccion.lower(),
         "elementos.nombre": elemento_body.nombre.lower()}) != 0:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El elemento '{seccion}/{elemento_body.nombre}' ya existe")

    carta.update_one(
        {"nombre": seccion.lower()},
        {"$pull": {"elementos": {"nombre": elemento.lower()}}})
    carta.update_one(
        {"nombre": seccion.lower()},
        {"$push": {"elementos": json_lower_encoder(elemento_body)}})

    return carta.find_one({"nombre": seccion})


@router.delete("/{seccion}/{elemento}", response_model=Seccion, response_model_exclude_unset=True)
def delete_elemento_seccion(seccion: str, elemento: str):
    section_obj = get_section(seccion)
    check_element_exists(seccion, elemento)
    carta.find_one_and_update({"nombre": seccion.lower()}, {"$pull": {"elementos": {"nombre": elemento.lower()}}})
    return section_obj


def get_section(section: str) -> Seccion:
    result = carta.find_one({"nombre": section.lower()})
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La sección '{section}', no existe.")
    return Seccion.parse_obj(result)


def check_section_exists(section: str):
    if carta.count_documents({"nombre": section.lower()}) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La sección '{section}', no existe.")


def check_element_exists(section: str, element: str):
    if carta.count_documents({"nombre": section.lower(), "elementos.nombre": element.lower()}) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El elemento '{section}/{element}', no existe.")


def check_precio(elemento: Elemento_carta):
    if elemento.precio is None:
        if elemento.variantes is None:
            raise AttributeError("Si el precio no está definido, debe haber variantes con precios")
        else:
            for variantes in elemento.variantes:
                for variante in variantes.variantes:
                    if variante.precio is None:
                        raise AttributeError(
                            f"Si el precio no está definido, todas las variantes deben tener precio.\nLa variante '{variante.descripcion}' no lo tiene definido")
                    elif variante.precio <= 0:
                        raise AttributeError(
                            f"El precio debe ser positivo.\nLa variante '{variante.descripcion}' tiene de precio: {variante.precio}")
    elif elemento.precio <= 0:
        raise AttributeError(f"El precio debe ser positivo. El precio es: {elemento.precio}")
    else:
        if elemento.variantes is not None:
            for variantes in elemento.variantes:
                for variante in variantes.variantes:
                    if variante.precio is not None:
                        raise AttributeError(
                            f"Si el precio está definido, ninguna variante puede tener precio.\nLa variante '{variante.descripcion}' tiene de precio: {elemento.precio}.")
