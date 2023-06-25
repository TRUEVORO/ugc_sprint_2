from http import HTTPStatus
from uuid import uuid4

import pytest
from pydantic import AnyHttpUrl
from tests.settings import test_settings

pytestmark = pytest.mark.asyncio

VIEWS_URL: AnyHttpUrl = test_settings.service_dsn + '/api/v1'


@pytest.mark.parametrize(
    'request_body, expected_status',
    [({'movie_id': str(uuid4()), 'user_id': str(uuid4()), 'viewed_frame': 100}, HTTPStatus.OK)],
)
async def test_view_progress(make_post_request, request_body, expected_status):
    """Test the view progress API endpoint."""

    _, status = await make_post_request(url='{}/{}'.format(VIEWS_URL, 'view_progress'), request_body=request_body)

    assert status == expected_status.value
