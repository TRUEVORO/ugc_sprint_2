from http import HTTPStatus

from fastapi import HTTPException


class ServiceError(HTTPException):
    pass


class ProducerError(ServiceError):
    """Error during data producing."""

    def __init__(self, detail: str = 'producer is unavailable, retry later', **kwargs):
        super().__init__(status_code=HTTPStatus.SERVICE_UNAVAILABLE, detail=detail, **kwargs)
