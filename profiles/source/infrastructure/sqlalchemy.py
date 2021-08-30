from sqlalchemy.ext.asyncio import create_async_engine

from source.infrastructure.settings import application_settings

engine = create_async_engine(
    application_settings.postgres_url,
    pool_size=50,
    max_overflow=0
)
