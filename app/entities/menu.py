# Import libraries

from fastapi import APIRouter, status, HTTPException
from app.database import db
from app.entities.models import Section, Element
from app.utils import json_lower_encoder

# Create router
router = APIRouter()

# Collections
menu = db["menu"]


# section
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Section, response_model_exclude_unset=True)
def create_section(section: Section):
    if menu.find_one({"name": section.name}) is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"La sección '{section.name}', ya existe.")

    if section.elements is not None:
        for element in section.elements:
            check_price(element)

    section_dict = json_lower_encoder(section)
    new_section = menu.insert_one(section_dict)
    created_section = menu.find_one({"_id": new_section.inserted_id})

    return created_section


@router.get("/", response_model=list[Section], response_model_exclude_unset=True)
def get_carta():
    return list(menu.find({}))


@router.get("/{section}", response_model=Section, response_model_exclude_unset=True)
def get_section(section: str):
    return get_section(section)


@router.get("/{section}/id")
def get_section_id(section: str):
    section_id = menu.find_one({"name": section}, {"_id": True})
    if section_id is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La sección '{section}', no existe.")
    return {"_id": str(section_id["_id"])}


@router.put("/{section}", response_model=Section, response_model_exclude_unset=True)
def update_section(section: str, section_body: Section):
    old_section_json = menu.find_one({"name": section.lower()})
    if old_section_json is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La sección '{section}', no existe.")
    old_section = Section.parse_obj(old_section_json)

    if section_body.name.lower() != old_section.name and menu.count_documents(
            {"name": section_body.name.lower()}) > 0:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"La sección '{section.name}', ya existe.")

    if section_body.elements is not None:
        for element in section.elements:
            check_price(element)

    new_section = json_lower_encoder(section_body)
    updated_secction = old_section.copy(update=new_section)
    menu.find_one_and_update(
        {"name": section.lower()},
        {"$set": json_lower_encoder(updated_secction)})

    return menu.find_one({"_id": old_section_json["_id"]})


@router.delete("/{section}", response_model=Section, response_model_exclude_unset=True)
def delete_section(section: str):
    section_obj = get_section(section)
    menu.delete_one({"name": section.lower()})
    return section_obj


# Elements
@router.post("/{section}", response_model=Section, response_model_exclude_unset=True)
def add_element_section(section: str, element: Element):
    check_section_exists(section)
    check_price(element)
    menu.find_one_and_update({"name": section.lower()}, {"$push": {"elements": json_lower_encoder(element)}})
    return menu.find_one({"name": section})


@router.put("/{section}/{element}", response_model=Section, response_model_exclude_unset=True)
def update_element_section(section: str, element: str, element_body: Element):
    check_section_exists(section)
    check_element_exists(section, element)
    check_price(element_body)

    if element.lower() != element_body.name.lower() \
            and menu.count_documents(
        {"name": section.lower(),
         "elements.name": element_body.name.lower()}) != 0:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El element '{section}/{element_body.name}' ya existe")

    menu.update_one(
        {"name": section.lower()},
        {"$pull": {"elements": {"name": element.lower()}}})
    menu.update_one(
        {"name": section.lower()},
        {"$push": {"elements": json_lower_encoder(element_body)}})

    return menu.find_one({"name": section})


@router.delete("/{section}/{element}", response_model=Section, response_model_exclude_unset=True)
def delete_element_section(section: str, element: str):
    section_obj = get_section(section)
    check_element_exists(section, element)
    menu.find_one_and_update({"name": section.lower()}, {"$pull": {"elements": {"name": element.lower()}}})
    return section_obj


def get_section(section: str) -> Section:
    result = menu.find_one({"name": section.lower()})
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La sección '{section}', no existe.")
    return Section.parse_obj(result)


def check_section_exists(section: str):
    if menu.count_documents({"name": section.lower()}) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La sección '{section}', no existe.")


def check_element_exists(section: str, element: str):
    if menu.count_documents({"name": section.lower(), "elements.name": element.lower()}) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El element '{section}/{element}', no existe.")


def check_price(element: Element):
    if element.price is None:
        if element.variants is None:
            raise AttributeError("Si el precio no está definido, debe haber variantes con precios")
        else:
            for variants in element.variants:
                for variant in variants.variants:
                    if variant.price is None:
                        raise AttributeError(
                            f"Si el precio no está definido, todas las variantes deben tener precio.\nLa variante '{variant.description}' no lo tiene definido")
                    elif variant.price <= 0:
                        raise AttributeError(
                            f"El precio debe ser positivo.\nLa variante '{variant.description}' tiene de precio: {variant.price}")
    elif element.price <= 0:
        raise AttributeError(f"El precio debe ser positivo. El precio es: {element.price}")
    else:
        if element.variants is not None:
            for variants in element.variants:
                for variant in variants.variants:
                    if variant.price is not None:
                        raise AttributeError(
                            f"Si el precio está definido, ninguna variante puede tener precio.\nLa variante '{variant.description}' tiene de precio: {element.price}.")
