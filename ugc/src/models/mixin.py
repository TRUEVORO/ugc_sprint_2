from uuid import UUID, uuid4

import orjson
from pydantic import BaseModel, Field


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class OrjsonMixin(BaseModel):
    """Model for fast json handling."""

    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class UUIDMixin(OrjsonMixin):
    """UUID mixin."""

    id: UUID = Field(default=uuid4(), alias='_id')
