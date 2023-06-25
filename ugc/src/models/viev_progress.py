from datetime import datetime
from uuid import UUID

from pydantic import Field

from .mixin import OrjsonMixin


class _ViewProgress(OrjsonMixin):
    """Base view progress."""

    movie_id: UUID
    user_id: UUID
    viewed_frame: int


class ViewProgressDto(_ViewProgress):
    """View progress dto."""

    event_time: datetime = Field(default_factory=datetime.now)


class ViewProgressRequest(_ViewProgress):
    """View progress request body."""

    pass
