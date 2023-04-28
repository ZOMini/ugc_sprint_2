from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    kafka_url: str = Field('localhost:9092')  # type: ignore[call-arg]
    kafka_client: str = Field('kafka-movies-api')  # type: ignore[call-arg]
    topic_list: list = Field(['views'])  # type: ignore[call-arg]
    project_name: str = Field('ugc_movies_api')  # type: ignore[call-arg]
    mongo_db: str = Field(...)  # type: ignore[call-arg]
    mongo_url: str = Field(...)  # type: ignore[call-arg]
    sentry_dns: str = Field(...)  # type: ignore[call-arg]
    logstash_host: str = Field(...)  # type: ignore[call-arg]
    logstash_port: int = Field(...)  # type: ignore[call-arg]
    log_level: str = Field('INFO')  # type: ignore[call-arg]

    class Config:
        env_file = '../.env'


settings = Settings()
kafka_list_urls = [settings.kafka_url]
