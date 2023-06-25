from http import HTTPStatus

from aiokafka.errors import KafkaError
from fastapi import APIRouter, Depends, HTTPException

from core import ProducerError
from models import ViewProgressDto, ViewProgressRequest
from services import ViewService, get_view_service

router = APIRouter(
    prefix='/api/v1',
    tags=['view'],
)


@router.post(
    '/view_progress',
    summary='Message about watching the film',
    description='Message about watching the film',
    response_model=None,
)
async def view_progress(
    request: ViewProgressRequest,
    view_service: ViewService = Depends(get_view_service),
) -> HTTPStatus | HTTPException:
    try:
        data = ViewProgressDto(movie_id=request.movie_id, user_id=request.user_id, viewed_frame=request.viewed_frame)
        await view_service.produce(data)
    except KafkaError:
        return ProducerError()

    return HTTPStatus.OK
