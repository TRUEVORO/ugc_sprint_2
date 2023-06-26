from bson import ObjectId

import orjson
from pydantic import BaseModel, Field, validator


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class OrjsonMixin(BaseModel):
    """Model for fast json handling."""

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class PyObjectId(ObjectId):
    """Py object id."""

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')


class ObjectIdMixin(BaseModel):
    """ObjectId mixin."""

    id: PyObjectId = Field(alias='_id')

    class Config(OrjsonMixin.Config):
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
