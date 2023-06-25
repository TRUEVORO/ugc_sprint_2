from pydantic import AnyHttpUrl, BaseSettings, Field


class TestSettings(BaseSettings):
    """Test settings class to read environment variables."""

    service_dsn: AnyHttpUrl = Field(default='http://localhost:81')

    kafka_topic: str = Field(default='progress')


test_settings = TestSettings()
