from uuid import uuid4, UUID

from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id:UUID = Field(default_factory=uuid4)
    email:EmailStr
    nickname:str
