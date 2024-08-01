from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field, computed_field

from telegram_bot.components.base.schema import BaseSchema


class CreateUserSchema(BaseSchema):
    id: int
    first_name: Optional[str] = Field(exclude=True, default=None)
    last_name: Optional[str] = Field(exclude=True, default=None)
    username: Optional[str] = None
    is_active: Optional[bool] = None

    @computed_field
    def name(self) -> str:
        return f"{self.first_name or ''} {self.last_name or ''}".strip() or str(self.id)


class UserSchema(BaseSchema):
    old_uuid: UUID = Field(alias='uuid', exclude=True)
    id: int
    name: str
    username: Optional[str] = None
    is_active: bool
    is_admin: bool
    old_created_at: Optional[datetime] = Field(alias='created_at', exclude=True, default=None)

    @computed_field
    def uuid(self) -> str:
        return str(self.old_uuid)

    @computed_field
    def created_at(self) -> str:
        return self.old_created_at.strftime("%d.%m.%Y %H:%M:%S")
