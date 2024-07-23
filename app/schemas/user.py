from tortoise import Tortoise
from typing import TypeAlias
from tortoise.contrib.pydantic import pydantic_model_creator

from app.models.user import User

Tortoise.init_models(["app.models"], "models")


UserResponse: TypeAlias = pydantic_model_creator(User, name="User")  # type: ignore
UserRequest: TypeAlias = pydantic_model_creator(User, name="UserRequest", exclude_readonly=True)  # type: ignore
