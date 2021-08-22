from pydantic import BaseSettings
from pydantic.networks import PostgresDsn


class ApplicationSettings(BaseSettings):
    postgres_url:PostgresDsn
    kafka_url:str

    class Config:
        env_file = '.env'

application_settings = ApplicationSettings()
