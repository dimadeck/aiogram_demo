from typing import Callable, Any, Awaitable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message


class CheckAdminMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        if user := data.get('user'):
            if user.is_admin:
                return await handler(event, data)
            else:
                await event.answer('Не хватает прав!')
