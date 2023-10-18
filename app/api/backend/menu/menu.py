# Import libraries

from fastapi import APIRouter, status, HTTPException
from app.db import db
from app.core.entities.menu import Section, Element
from app.lib.utils import json_lower_encoder, remove_non_letters_and_replace_spaces

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
    sections = list(menu.find({"parent": {"$exists": False}}, {"_id": False}).sort("name"))
    subsections = list(menu.find({"parent": {"$exists": True}}, {"_id": False}).sort("name"))
    return sort_menu(sections, subsections)


@router.get("/{section}", response_model=Section, response_model_exclude_unset=True)
def get_section(section: str, ids: bool = False):
    section_obj = _get_section(section)
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
    old_section = Section.model_validate(old_section_json)

    if section_body.name.lower() != old_section.name and menu.count_documents(
            {"name": section_body.name.lower()}) > 0:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"La sección '{section.name}', ya existe.")

    if section_body.elements is not None:
        for element in section_body.elements:
            check_price(element)

    new_section = json_lower_encoder(section_body)
    updated_secction = old_section.model_copy(update=new_section)
    menu.find_one_and_update(
        {"name": section.lower()},
        {"$set": json_lower_encoder(updated_secction)})

    return menu.find_one({"_id": old_section_json["_id"]})


@router.delete("/{section}", response_model=Section, response_model_exclude_unset=True)
def delete_section(section: str):
    section_obj = _get_section(section)
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
    section_obj = _get_section(section)
    check_element_exists(section, element)
    menu.find_one_and_update({"name": section.lower()}, {"$pull": {"elements": {"name": element.lower()}}})
    return section_obj


def _get_section(section: str) -> Section:
    result = menu.find_one({"name": section.lower()}, {"_id": False})
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La sección '{section}', no existe.")
    return Section.model_validate(result)


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


def check_positive_price(price: float, message: str):
    if price <= 0:
        raise AttributeError(message)


def check_no_variant_price(variant_group):
    for variant in variant_group.variants:
        if variant.price is not None:
            raise AttributeError(
                f"Element price is defined, but in {variant_group.name} "
                f"{variant.name} has a price: {variant.price}.")


def check_all_variants_price_defined(variant_group):
    variants_with_price = sum(variant.price is not None for variant in variant_group.variants)
    total_variants = len(variant_group.variants)

    if variants_with_price == total_variants:
        return True
    elif variants_with_price > 0:
        raise AttributeError(
            f"In a Variants group, either all Variants must have a price or none should have a price, "
            f"but in {variant_group.name} there are some variants with price, but others that do not")
    return False


def check_price(element: Element):
    if element.price is None:
        if element.variants is None:
            raise AttributeError("Element price is not defined and there are no Variants.")

        price_defined_variants_group = sum(check_all_variants_price_defined(variant_group)
                                           for variant_group in element.variants)

        if price_defined_variants_group != 1:
            raise AttributeError(
                "There must be exactly one Variants group with all its Variants having prices defined.")
        return

    check_positive_price(element.price, f"Element price must be positive: {element.price}.")
    if element.variants is None:
        return

    for variant_group in element.variants:
        check_no_variant_price(variant_group)


def sort_menu(sections, subsections):
    # Create a dictionary where the key is the section name and the value is a list of subsections
    sections_with_subsections = {section["name"]: [] for section in sections}

    # Populate the dictionary with the corresponding subsections
    for subsection in subsections:
        parent_section = subsection["parent"]
        if parent_section in sections_with_subsections:
            sections_with_subsections[parent_section].append(subsection)
        else:
            print(f"Warning: Subsection {subsection['name']} has a non-existent parent section: {parent_section}")

    # Create an ordered list where for each section the section and its subsections are added
    ordered_menu = []
    for section in sections:
        ordered_menu.append(section)
        ordered_menu.extend(sections_with_subsections[section["name"]])

    return ordered_menu

