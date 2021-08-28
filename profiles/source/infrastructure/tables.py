from uuid import uuid4, UUID
from typing import Optional

from sqlmodel import Field, SQLModel


class ProfileTable(SQLModel, table=True):
    id:UUID = Field(default_factory=uuid4, primary_key=True)
    user_id:UUID
    bio:Optional[str] = Field(default=None, index=False)
    age:Optional[int] = Field(default=None, index=False)
    gender:Optional[str] = Field(default=None, index=False)

    __tablename__ = 'profiles'
