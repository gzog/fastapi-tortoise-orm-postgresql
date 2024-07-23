from tortoise import Tortoise
from typing import TypeAlias
from tortoise.contrib.pydantic import pydantic_model_creator

from app.models.user import User

Tortoise.init_models(["app.models"], "models")


UserResponse: TypeAlias = pydantic_model_creator(User, name="User", exclude=["password"])  # type: ignore
UserCreateRequest: TypeAlias = pydantic_model_creator(User, name="UserCreateRequest", exclude_readonly=True)  # type: ignore
UserUpdateRequest: TypeAlias = pydantic_model_creator(User, name="UserUpdateRequest", exclude=["username"], exclude_readonly=True)  # type: ignore
