from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        openapi_url="/openapi.json",
        docs_url="/docs/",
        redoc_url=None,
    )

    register_tortoise(
        app,
        db_url=settings.DB_URL,
        modules={"models": ["app.note.models"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )

    register_views(app=app)

    return app


def register_views(app: FastAPI):
    from app.note.views import note_views

    app.include_router(note_views, prefix="/notes", tags=["Notes"])


app = create_app()
