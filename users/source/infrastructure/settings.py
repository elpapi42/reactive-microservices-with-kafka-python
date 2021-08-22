from pydantic import BaseSettings
from pydantic.networks import PostgresDsn


class ApplicationSettings(BaseSettings):
    postgres_url:PostgresDsn

    class Config:
        env_file = '.env'

application_settings = ApplicationSettings()
