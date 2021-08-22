from uuid import uuid4
import pytest

from source.adapters.repositories import FakeUserRepository
from source.application.register_user import RegisterUserService


@pytest.mark.asyncio
async def test_register_user_service():
    repo = FakeUserRepository()

    service = RegisterUserService(repo)

    output = await service.execute(email='test@email.com', nickname='test_name')

    saved_user = await repo.get(output.id)

    assert saved_user is not None
    assert output.email == 'test@email.com'
    assert output.nickname == 'test_name'
    assert output.id == saved_user.id
