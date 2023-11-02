from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.user.models import User

UserResponse = pydantic_model_creator(User, name="User")  # type: ignore
UserRequest = pydantic_model_creator(User, name="UserRequest", exclude_readonly=True)  # type: ignore


class Status(BaseModel):
    message: str
