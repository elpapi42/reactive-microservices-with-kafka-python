from uuid import UUID
from typing import Optional

from sqlmodel import Field, SQLModel


class ProfileModel(SQLModel, table=True):
    user_id:UUID = Field(primary_key=True)
    bio:Optional[str] = Field(default=None, index=False)
    age:Optional[int] = Field(default=None, index=False)
    gender:Optional[str] = Field(default=None, index=False)

    __tablename__ = 'profiles'
