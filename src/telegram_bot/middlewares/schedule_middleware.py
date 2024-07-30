from typing import Callable, Any, Awaitable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message


class SchedulerMiddleware(BaseMiddleware):
    def __init__(self, scheduler):
        self.scheduler = scheduler

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        data['scheduler'] = self.scheduler
        return await handler(event, data)
