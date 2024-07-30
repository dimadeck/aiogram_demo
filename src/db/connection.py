import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base, sessionmaker
from utils.config import settings

engine = create_async_engine(settings.dsn, future=True)
async_session = async_sessionmaker(engine, expire_on_commit=False, autocommit=False, class_=AsyncSession)

# sync_engine = create_engine(settings.sync_dsn, future=True)
# sync_session = sessionmaker(sync_engine, expire_on_commit=False, autocommit=False)
metadata = sqlalchemy.MetaData()
Base = declarative_base(metadata=metadata)
