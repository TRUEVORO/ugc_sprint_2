from motor.motor_asyncio import AsyncIOMotorClient

from .base_repository import AsyncBaseRepository


class MongoRepository(AsyncBaseRepository):
    """Interface for mongo repository."""

    def __init__(self, mongo: AsyncIOMotorClient, table: str) -> None:
        """Initialize Mongo repository."""

        self.mongo: AsyncIOMotorClient = mongo[table]

    async def create(self, data: dict) -> dict:
        """Create new object with given arguments."""

        return await self.mongo.insert_one(data)

    async def retrieve(self, query: dict) -> dict | None:
        """Retrieve object based on given arguments."""

        return await self.mongo.find_one(query)

    async def retrieve_many(self, query: dict, skip: int = 0, limit: int = 100) -> list[dict] | None:
        """Retrieve multiple objects based on given arguments."""

        cursor = self.mongo.find(query).skip(skip).limit(limit)
        return await cursor.to_list(length=None)

    async def update(self, query: dict, data: dict, method: str = '$set') -> dict:
        """Update existing object with given arguments."""

        return await self.mongo.find_one_and_update(query, {method: data})

    async def delete(self, query: dict) -> dict:
        """Delete object based on given arguments."""

        return await self.mongo.find_one_and_delete(query)
