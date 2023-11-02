from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.user.models import User

UserResponse = pydantic_model_creator(User, name="User")
UserRequest = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)


class Status(BaseModel):
    message: str
