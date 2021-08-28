from uuid import uuid4, UUID
from typing import Optional

from pydantic import BaseModel, Field

from source.domain.enums import Gender


class Profile(BaseModel):
    id:UUID = Field(default_factory=uuid4)
    owner:UUID
    bio:Optional[str] = None
    age:Optional[int] = None
    gender:Optional[Gender] = None
