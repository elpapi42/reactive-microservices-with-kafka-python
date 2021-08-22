from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Table, Column, String

from source.infrastructure.sqlalchemy import metadata


users_table = Table('users', metadata,
    Column('id', UUID(), primary_key=True),
    Column('email', String()),
    Column('nickname', String()),
)
