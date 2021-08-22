from uuid import UUID
from typing import Dict, Optional
from dataclasses import dataclass, field

from source.infrastructure.databases import postgres_database
#from source.infrastructure.tables import users_table
from source.domain.entities import User
from source.ports.repositories import UserRepository


@dataclass
class FakeUserRepository(UserRepository):

    registry:Dict[int, User] = field(default_factory=dict)

    async def add(self, user:User):
        self.registry[hash(user.id)] = user

    async def get(self, id:UUID) -> Optional[User]:
        try:
            user = self.registry[hash(id)]
        except KeyError:
            user = None
        return user
