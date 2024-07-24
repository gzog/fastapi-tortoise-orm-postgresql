from tortoise import fields

from backend.models.base import Base
from backend.models.mixins import TimestampsMixin


class Publication(Base, TimestampsMixin):
    title = fields.CharField(max_length=30)
    user: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        "models.User", related_name="publications"
    )

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title
