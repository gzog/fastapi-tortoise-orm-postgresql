from tortoise import Tortoise
from typing import TypeAlias
from tortoise.contrib.pydantic import pydantic_model_creator

from backend.models.user import User


UserResponse: TypeAlias = pydantic_model_creator(User, name="User", exclude=["password"])  # type: ignore
UserCreateRequest: TypeAlias = pydantic_model_creator(User, name="UserCreateRequest", exclude_readonly=True)  # type: ignore
UserUpdateRequest: TypeAlias = pydantic_model_creator(User, name="UserUpdateRequest", exclude=["username"], exclude_readonly=True)  # type: ignore
