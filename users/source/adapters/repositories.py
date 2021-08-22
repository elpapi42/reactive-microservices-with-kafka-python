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
        self.registry[hash(user)] = user

    async def get(self, id:UUID) -> Optional[User]:
        try:
            user = [user for user in self.registry.values() if user.id == id][0]
        except IndexError:
            user = None
        return user
