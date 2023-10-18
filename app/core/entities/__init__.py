from typing import Annotated, Union, Any

from bson import ObjectId
from pydantic import AfterValidator, PlainSerializer, WithJsonSchema, BaseModel, ConfigDict, Field


def validate_object_id(v: Any) -> ObjectId:
    if isinstance(v, ObjectId):
        return v
    if ObjectId.is_valid(v):
        return ObjectId(v)
    raise ValueError("Invalid ObjectId")


PyObjectId = Annotated[
    Union[str, ObjectId],
    AfterValidator(validate_object_id),
    PlainSerializer(lambda x: str(x), return_type=str),
    WithJsonSchema({"type": "string"}, mode="serialization"),
]

class ComplexModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)


class Id(ComplexModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    model_config = ConfigDict(populate_by_name=True)
