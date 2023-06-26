from abc import ABC, abstractmethod


class AsyncBaseRepository(ABC):
    """Base interface for async repository."""

    @abstractmethod
    async def create(self, *args, **kwargs):
        """Create new object with given arguments."""

        raise NotImplementedError

    @abstractmethod
    async def retrieve(self, *args, **kwargs):
        """Retrieve object based on given arguments."""

        raise NotImplementedError

    @abstractmethod
    async def retrieve_many(self, *args, **kwargs):
        """Retrieve multiple objects based on given arguments."""

        raise NotImplementedError

    @abstractmethod
    async def update(self, *args, **kwargs):
        """Update existing object with given arguments."""

        raise NotImplementedError

    @abstractmethod
    async def delete(self, *args, **kwargs):
        """Delete object based on given arguments."""

        raise NotImplementedError
