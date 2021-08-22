from uuid import UUID
from dataclasses import dataclass

from pydantic import BaseModel

from source.domain.entities import User
from source.ports.repositories import UserRepository


class RegisterUserServiceOutputDTO(BaseModel):
    id:UUID
    email:str
    nickname:str

@dataclass
class RegisterUserService():
    repo:UserRepository

    async def execute(self, email:str, nickname:str) -> User:
        user = User(email=email, nickname=nickname)

        await self.repo.add(user)

        return RegisterUserServiceOutputDTO(**user.dict())
