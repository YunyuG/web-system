from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, Field
from config import db_settings

url = f"postgresql+asyncpg://{db_settings.username}:{db_settings.password}@{db_settings.host}:{db_settings.port}/{db_settings.database}"
engine = create_async_engine(url=url, echo=True)

sessionmaker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

# @asynccontextmanager
async def get_session():
    try:
        session = sessionmaker()
        yield session
        await session.commit()
    except SQLAlchemyError:
        await session.rollback()
        raise
    finally:
        await session.close()
