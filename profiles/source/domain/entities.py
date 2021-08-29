from uuid import UUID
from typing import Optional

from pydantic import BaseModel

from source.domain.enums import Gender


class Profile(BaseModel):
    user_id:UUID
    bio:Optional[str] = None
    age:Optional[int] = None
    gender:Optional[Gender] = None
