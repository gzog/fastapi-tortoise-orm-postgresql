from tortoise import fields
from app.models.mixins import TimestampsMixin
from app.models.base import Base
from app.models.user import User


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
