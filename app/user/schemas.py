from pydantic import BaseModel
from app.user.models import Users
from tortoise.contrib.pydantic import pydantic_model_creator

UserResponse = pydantic_model_creator(Users, name="User")
UserRequest = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)


class Status(BaseModel):
    message: str
