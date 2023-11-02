from passlib.hash import bcrypt
from tortoise import fields

from app.core.models import BaseModel


class User(BaseModel):
    """
    The User model
    """

    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    name = fields.CharField(max_length=50, null=True)
    family_name = fields.CharField(max_length=50, null=True)
    category = fields.CharField(max_length=30, default="misc")
    password_hash = fields.CharField(max_length=128, null=True)

    def full_name(self) -> str:
        """
        Returns the best name
        """
        if self.name or self.family_name:
            return f"{self.name or ''} {self.family_name or ''}".strip()
        return self.username

    def verify_password(self, password) -> bool:
        return bcrypt.verify(password, self.password_hash)

    class PydanticMeta:
        computed = ["full_name"]
        exclude = ["password_hash", "created_at", "updated_at"]
