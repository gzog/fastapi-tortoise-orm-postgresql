import bcrypt
from app.models.user import User


class UserRepository:
    @classmethod
    async def create(cls, payload: dict) -> User:
        user = await User.create(**payload)
        user.password = bcrypt.hash(payload['password'])
        return await user.save()

    @classmethod
    async def update(cls, user: User) -> User:
        user.save()

    @classmethod
    async def get_by_id(cls, id) -> User:
        return await User.get_or_none(id=id).prefetch_related("publications", "address")

    @classmethod
    async def get_all(cls) -> list[User]:
        users = await User.all().prefetch_related("publications", "address")
        return users

    @classmethod
    async def delete(cls, id) -> int:
        return await User.filter(id=id).delete()
