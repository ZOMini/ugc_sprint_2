from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    kafka_url: str = Field('localhost:9092')
    kafka_client: str = Field('kafka-movies-api')
    topic_list: list = Field(['views'])
    project_name: str = Field(...)
    mongo_db: str = Field(...)
    mongo_url: str = Field(...)

    class Config:
        env_file = '../.env'


settings = Settings()
kafka_list_urls = [settings.kafka_url]
