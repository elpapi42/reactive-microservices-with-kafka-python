from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from source.domain.enums import Gender


class ProfileOutputDTO(BaseModel):
    user_id:UUID
    bio:Optional[str]
    age:Optional[int]
    gender:Optional[Gender]
