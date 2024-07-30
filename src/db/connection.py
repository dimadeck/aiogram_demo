import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

from utils.config import settings

engine = create_async_engine(settings.dsn, future=True)
async_session = async_sessionmaker(engine, expire_on_commit=False, autocommit=False, class_=AsyncSession)

metadata = sqlalchemy.MetaData()
Base = declarative_base(metadata=metadata)
