from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app import settings
from app.api.user import router as user_router


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
        modules={"models": ["app.models"]},
        generate_schemas=False,
        add_exception_handlers=False,
    )

    register_views(app=app)

    return app


def register_views(app: FastAPI) -> None:
    app.include_router(user_router, prefix="/users", tags=["Users"])


app = create_app()
