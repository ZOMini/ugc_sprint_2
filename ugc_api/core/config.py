from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    kafka_url: str = Field('localhost:9092')  # noqa: call-arg
    kafka_client: str = Field('kafka-movies-api')  # noqa: call-arg
    topic_list: list = Field(['views'])  # noqa: call-arg
    project_name: str = Field('ugc_movies_api')  # noqa: call-arg
    mongo_db: str = Field(...)  # noqa: call-arg
    mongo_url: str = Field(...)  # noqa: call-arg
    sentry_dns: str = Field(...)  # noqa: call-arg
    logstash_host: str = Field(...)  # noqa: call-arg
    logstash_port: int = Field(...)  # noqa: call-arg
    log_level: str = Field('INFO')  # noqa: call-arg

    class Config:
        env_file = '../.env'


settings = Settings()
kafka_list_urls = [settings.kafka_url]
