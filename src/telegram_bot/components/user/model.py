from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, String, Boolean, DateTime, UUID, BigInteger

from db.connection import Base


class TelegramUserModel(Base):
    __tablename__ = "telegram_users"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    id = Column(BigInteger, nullable=False)
    name = Column(String, nullable=False)
    username = Column(String, nullable=True, default=None)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
