import hashlib
import json
from pprint import pprint

from app.api.frontend.entities.order import ExtendedElement
from app.core.entities.menu import Section
from app.core.entities.order import Element, BasicElement
from app.lib.utils import json_lower_encoder


def encode(string: str):
    hash_obj = hashlib.sha256(string.encode())
    return hash_obj.hexdigest()


def generate_element_id_from_names(section: str, element: str) -> str:
    composed_name = section + element
    return encode(composed_name)


def generate_element_id(element: BasicElement) -> str:
    if isinstance(element, Element):
        element = basic_element_from_element(element)
    json_str = json.dumps(json_lower_encoder(element), sort_keys=True)
    return encode(json_str)


def basic_element_from_element(element: Element) -> BasicElement:
    return BasicElement(**json_lower_encoder(element))


def extend_element(element: Element) -> ExtendedElement:
    quantity = element.quantity
    json_element = json_lower_encoder(element)
    extended_element = ExtendedElement(**json_element)
    extended_element.id = generate_element_id(element)
    extended_element.quantity = quantity
    return extended_element


def generate_extend_elements_with_images(sections: list[Section], command: list[Element]) -> list[ExtendedElement]:
    image_dict = {}
    for section in sections:
        if section.elements is not None:
            for element in section.elements:
                image_dict[(section.name, element.name)] = element.image
    elements_with_image = []
    for element in command:
        extended_element = extend_element(element)
        extended_element.image = image_dict[(element.section, element.element)]
        elements_with_image.append(extended_element)
    return elements_with_image
