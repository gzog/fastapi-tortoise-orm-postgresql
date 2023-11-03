from passlib.hash import bcrypt
from tortoise import fields, models


class TimestampsMixin:
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class User(models.Model):
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

    def verify_password(self, password) -> bool:
        return bcrypt.verify(password, self.password)

    class PydanticMeta:
        computed = ["full_name"]
        exclude = ["created_at", "updated_at"]


class Address(models.Model):
    city = fields.CharField(max_length=64)
    street = fields.CharField(max_length=128)

    user: fields.OneToOneRelation[User] = fields.OneToOneField(
        "models.User",
        on_delete=fields.OnDelete.CASCADE,
        related_name="address",
    )

    class Meta:
        ordering = ["city"]


class Publication(models.Model):
    title = fields.CharField(max_length=30)
    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", related_name="publications"
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = fields.CharField(max_length=100)
    publications: fields.ManyToManyRelation[Publication] = fields.ManyToManyField(
        "models.Publication", related_name="articles", through="article_publication"
    )

    class Meta:
        ordering = ["headline"]

    def __str__(self):
        return self.headline
