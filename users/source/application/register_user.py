from typing import Optional
from uuid import UUID
from dataclasses import dataclass

from pydantic import BaseModel

from source.domain.entities import User
from source.ports.repositories import UserRepository
from source.ports.events import UserRegisteredEvent


class RegisterUserServiceOutputDTO(BaseModel):
    id:UUID
    email:str
    nickname:str

@dataclass
class RegisterUserService():
    repo:UserRepository
    user_registered_event:Optional[UserRegisteredEvent] = None

    async def execute(self, email:str, nickname:str) -> User:
        user = User(email=email, nickname=nickname)

        await self.repo.add(user)

        if self.user_registered_event:
            await self.user_registered_event.trigger(user=user)

        return RegisterUserServiceOutputDTO(**user.dict())
