from typing import Callable, Any, Awaitable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message

from utils.logging import get_log_channel

log = get_log_channel('Aiogram Demo Launcher')


class LoggerMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        log.info(f'New message: [{event.from_user.username} ({event.from_user.id})]: {event.text}')
        log.debug(f'Raw event: {event}')
        log.debug(f'Data: {data}')
        return await handler(event, data)
