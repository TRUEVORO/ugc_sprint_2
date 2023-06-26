from motor.motor_asyncio import AsyncIOMotorCollection
from core import settings

mongo: AsyncIOMotorCollection | None = None


def get_mongo() -> AsyncIOMotorCollection:
    """Get mongo."""

    return mongo[settings.mongo_db]  # noqa
