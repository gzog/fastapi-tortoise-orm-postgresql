from backend.models.base import Base
from backend.models.publication import Publication
from backend.models.mixins import TimestampsMixin
from tortoise import fields

from passlib.hash import bcrypt


class User(Base, TimestampsMixin):
    """
    The User model
    """

    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    name = fields.CharField(max_length=50, null=True)
    family_name = fields.CharField(max_length=50, null=True)
    password = fields.CharField(max_length=128, null=False)

    # It is useful to define the reverse relations manually so that type checking
    #  and auto completion work
    publications: fields.ReverseRelation["Publication"]

    def full_name(self) -> str:
        """
        Returns the best name
        """
        if self.name or self.family_name:
            return f"{self.name or ''} {self.family_name or ''}".strip()
        return self.username

    def verify_password(self, password: str) -> bool:
        return bcrypt.verify(password, self.password)

    class PydanticMeta:
        exclude = ["created_at", "updated_at"]
