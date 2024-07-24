from tortoise import fields
from backend.models.mixins import TimestampsMixin
from backend.models.base import Base
from backend.models.user import User


class Address(Base, TimestampsMixin):
    city = fields.CharField(max_length=64)
    street = fields.CharField(max_length=128)

    user: fields.OneToOneRelation[User] = fields.OneToOneField(
        "models.User",
        on_delete=fields.OnDelete.CASCADE,
        related_name="address",
    )

    class Meta:
        ordering = ["city"]
