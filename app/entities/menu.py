# Import libraries

from fastapi import APIRouter, status, HTTPException
from app.database import db
from app.entities.models import Section, Element
from app.utils import json_lower_encoder, remove_non_letters_and_replace_spaces

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


@router.get("/sections", response_model=list[Section], response_model_exclude_unset=True)
def get_sections():
    return list(menu.find({}, {"elements": False}))


@router.get("/active", response_model=list[Section], response_model_exclude_unset=True)
def get_active():
    return list(menu.find_one({""}, {"elements": False}))


@router.get("/{section}", response_model=Section, response_model_exclude_unset=True)
def get_section(section: str, ids: bool = False):
    section_obj = get_section(section)
    if ids:
        for element in section_obj.elements:
            add_element_id(element)
    return section_obj


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
        for element in section_body.elements:
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
    check_element_not_exists(section, element.name)
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
            detail=f"El elemento '{section}/{element}', no existe.")


def check_element_not_exists(section: str, element: str):
    if menu.count_documents({"name": section.lower(), "elements.name": element.lower()}) > 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El elemento '{section}/{element}', ya existe.")


def add_element_id(element: Element):
    element.id = remove_non_letters_and_replace_spaces(element.name)


def check_price(element: Element):
    if element.price is not None:
        if element.price <= 0:
            raise AttributeError(f"Element price must be positive: {element.price}.")

        # If the Element price is defined, no Variant should have a price
        if element.variants is not None:
            for variant_group in element.variants:
                for variant in variant_group.variants:
                    if variant.price is not None:
                        raise AttributeError(
                            f"Element price is defined, "
                            f"but in {variant_group.name} {variant.description} has a price: {variant.price}.")
    else:
        # If the Element price is not defined,
        # there should be at least one Variants with all its Variant having prices defined
        if element.variants is not None:
            price_defined_variants_group = 0
            for variant_group in element.variants:
                variants_with_price = 0
                total_variants = len(variant_group.variants)
                for variant in variant_group.variants:
                    if variant.price is not None:
                        if variant.price <= 0:
                            raise AttributeError(
                                f"Variant price must be positive, "
                                f"but in {variant_group.name} {variant.description} has a price: {variant.price}.")
                        variants_with_price += 1

                if variants_with_price == total_variants:
                    price_defined_variants_group += 1
                elif variants_with_price > 0:
                    raise AttributeError(
                        f"In a Variants group, either all Variants must have a price or none should have a price, "
                        f"but in {variant_group.name} there are some variants with price, but others that do not")

            if price_defined_variants_group != 1:
                raise AttributeError(
                    "There must be exactly one Variants group with all its Variants having prices defined.")
        else:
            raise AttributeError("Element price is not defined and there are no Variants.")
