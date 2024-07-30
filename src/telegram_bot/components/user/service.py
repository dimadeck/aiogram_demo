from typing import Any

from telegram_bot.components.base.crud import BaseCRUD
from telegram_bot.components.user.model import TelegramUserModel
from telegram_bot.components.user.schema import CreateUserSchema, UserSchema


class UserService(BaseCRUD):
    MODEL = TelegramUserModel

    async def create_user(self, user_data: dict[str, Any]) -> TelegramUserModel:
        data = CreateUserSchema(**user_data, is_active=True).model_dump()
        return await self._create(**data)

    async def get_user(self, user_id: int) -> TelegramUserModel:
        return await self._get_one(dict(id=user_id))

    async def get_or_create_user(self, user_data: dict[str, Any]) -> UserSchema:
        try:
            user_id = user_data['id']
            user = await self.get_user(user_id)
        except Exception as e:
            user = await self.create_user(user_data)
        return UserSchema.model_validate(user)

    async def change_admin_role(self, user_id: int, is_admin: bool) -> UserSchema:
        user = await self._update(
            search_fields=dict(id=user_id),
            is_admin=is_admin,
        )
        return UserSchema.model_validate(user)

    async def get_all_users(self) -> list[UserSchema]:
        users = await self._get_many({})
        return [UserSchema.model_validate(user) for user in users]
