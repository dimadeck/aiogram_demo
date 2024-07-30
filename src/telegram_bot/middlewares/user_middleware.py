from typing import Callable, Any, Awaitable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message

from telegram_bot.components.user.service import UserService


class UserMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        data['user'] = await UserService().get_or_create_user(event.from_user.model_dump())
        return await handler(event, data)
