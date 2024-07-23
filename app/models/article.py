from tortoise import fields

from app.models.base import Base
from app.models.publication import Publication
from app.models.mixins import TimestampsMixin


class Article(Base, TimestampsMixin):
    headline = fields.CharField(max_length=100)
    publications: fields.ManyToManyRelation[Publication] = fields.ManyToManyField(
        "models.Publication", related_name="articles", through="article_publication"
    )

    class Meta:
        ordering = ["headline"]

    def __str__(self) -> str:
        return self.headline
