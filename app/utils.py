import json, re
from fastapi.encoders import jsonable_encoder


def dict_to_lower(dict: dict) -> dict:
    return json.loads(json.dumps(dict).lower())


def json_encoder(obj) -> dict:
    return jsonable_encoder(obj, exclude_unset=True, exclude_defaults=True)


def json_lower_encoder(obj) -> dict:
    return dict_to_lower(json_encoder(obj))

def remove_non_letters_and_replace_spaces(value):
    filtered_str = re.sub(r"[^a-zA-Z\s]", "", value)
    result = re.sub(r"\s+", "_", filtered_str)
    return result

