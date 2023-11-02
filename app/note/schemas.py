from pydantic.main import BaseModel


class Note(BaseModel):
    id: int | None
    title: str | None = None
    data: str

    class Config:
        from_attributes = True
