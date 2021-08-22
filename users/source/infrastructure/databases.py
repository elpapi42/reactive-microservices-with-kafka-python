from databases import Database

from source.infrastructure.settings import application_settings


postgres_database = Database(application_settings.postgres_url)
