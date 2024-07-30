from typing import Callable, Any, Awaitable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message

from utils.config import settings


class ExceptionMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        try:
            return await handler(event, data)
        except Exception as e:
            print(f"Handle message error: {str(e)}")
            if settings.DEBUG:
                await event.answer(f'Ошибка: {str(e)}')
            await event.answer('Произошла ошибка, попробуйте позже!')
