import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

load_dotenv()


def _build_db_url() -> str:
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    return f"mysql+aiomysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"


SQLALCHEMY_DATABASE_URL = _build_db_url()

DB_PARAMS = {}

engine: AsyncEngine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, **DB_PARAMS, echo=False
)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
