from tortoise import fields
from tortoise.models import Model


class Note(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=1000)
    data = fields.CharField(max_length=10000)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self) -> str:
        return self.data
