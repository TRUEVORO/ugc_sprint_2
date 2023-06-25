from abc import ABC, abstractmethod


class AsyncBaseProducer(ABC):
    """Async base broker producer."""

    @abstractmethod
    async def produce(self, *args, **kwargs):
        """Produce method."""

        raise NotImplementedError
