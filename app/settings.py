APP_NAME = "Notes"
APP_VERSION = "0.0.2"
POSTGRESQL_HOSTNAME = "localhost"
POSTGRESQL_USERNAME = "postgres"
POSTGRESQL_PASSWORD = "postgres"
POSTGRESQL_DATABASE = "notesdb"

DB_URL = f"postgres://{POSTGRESQL_USERNAME}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_HOSTNAME}:5432/{POSTGRESQL_DATABASE}"

TORTOISE_ORM = {
    "connections": {"default": DB_URL},
    "apps": {
        "models": {
            "models": ["app.note.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
