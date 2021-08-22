from typing import List
from uuid import UUID

from pydantic import BaseModel
from fastapi import APIRouter
from pydantic.networks import EmailStr

from source.adapters.repositories import FakeUserRepository
from source.application.register_user import RegisterUserService


router = APIRouter()

class UserSchemaIn(BaseModel):
    email:EmailStr
    nickname:str

class UserSchemaOut(BaseModel):
    id:UUID
    email:EmailStr
    nickname:str

@router.post('/users', status_code=201, response_model=UserSchemaOut)
async def register_user(data:UserSchemaIn):
    repo = FakeUserRepository()
    service = RegisterUserService(repo)

    user = await service.execute(**data.dict())

    return UserSchemaOut(**user.dict())
