from passlib.hash import bcrypt
from tortoise.exceptions import IntegrityError
from backend.models.user import User


class UserRepository:
    @classmethod
    async def create(cls, payload: dict) -> User | None:
        try:
            user = await User.create(**payload)
        except IntegrityError:
            return None
        user.password = bcrypt.hash(payload["password"])
        await user.save()
        await user.fetch_related("publications", "address")
        return user

    @classmethod
    async def update(cls, user_id: int, payload: dict) -> User:
        user = await cls.get_by_id(user_id)
        if not user:
            return None
        user.__dict__.update(**payload)
        await user.save()
        return user

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
