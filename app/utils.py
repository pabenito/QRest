import json
from fastapi.encoders import jsonable_encoder


def dict_to_lower(dict: dict) -> dict:
    return json.loads(json.dumps(dict).lower())


def json_encoder(obj) -> dict:
    return jsonable_encoder(obj, exclude_unset=True, exclude_defaults=True)


def json_lower_encoder(obj) -> dict:
    return dict_to_lower(json_encoder(obj))
