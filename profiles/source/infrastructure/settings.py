from pydantic import BaseSettings


class ApplicationSettings(BaseSettings):
    postgres_url:str
    postgres_migrations_url:str
    kafka_url:str

    class Config:
        env_file = '.env'

application_settings = ApplicationSettings()
