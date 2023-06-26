from typing import TypeVar
from uuid import UUID

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from models import UUIDMixin
from .base_repository import AsyncBaseRepository


DatabaseModel = TypeVar('DatabaseModel', bound=UUIDMixin)


class MongoRepository(AsyncBaseRepository):
    """Interface for mongo repository."""

    def __init__(self, mongo: AsyncIOMotorClient, table: str) -> None:
        """Initialize Mongo repository."""

        self.mongo: AsyncIOMotorClient = mongo[table]

    async def create(self, data: DatabaseModel) -> dict:
        """Create new object with given arguments."""

        return self.mongo.insert_one(data.dict())

    async def retrieve(self, uuid: UUID) -> dict | None:
        """Retrieve object based on given arguments."""

        return await self.mongo.find_one({'_id': ObjectId(str(uuid))})

    async def retrieve_many(self, query: dict, skip: int = 0, limit: int = 100) -> list[dict] | None:
        """Retrieve multiple objects based on given arguments."""

        cursor = self.mongo.find(query).skip(skip).limit(limit)
        return await cursor.to_list(length=None)

    async def update(self, uuid: UUID, data: dict, method: str = '$set') -> dict:
        """Update existing object with given arguments."""

        return await self.mongo.update_one({'_id': ObjectId(str(uuid))}, {'$set': data})

    async def delete(self, uuid: UUID) -> dict:
        """Delete object based on given arguments."""

        return await self.mongo.delete_one({'_id': ObjectId(str(uuid))})
