from pydantic import BaseModel
from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

from app.models import User

Tortoise.init_models(["app.models"], "models")

UserResponse = pydantic_model_creator(User, name="User")  # type: ignore
UserRequest = pydantic_model_creator(User, name="UserRequest", exclude_readonly=True)  # type: ignore


class Status(BaseModel):
    message: str
