from aiogram import Bot
from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from telegram_bot.commands import set_commands
from telegram_bot.components.admin.router import router as admin_router
from telegram_bot.components.base.router import router as default_router
from telegram_bot.components.image.router import router as image_router
from telegram_bot.components.inline.router import router as inline_router
from telegram_bot.components.scheduler.handler import daily_message
from telegram_bot.components.scheduler.router import router as scheduler_router
from telegram_bot.components.state.router import router as state_router
from telegram_bot.components.user.router import router as user_router
from telegram_bot.components.weather.router import router as weather_router
from telegram_bot.middlewares.exception_middleware import ExceptionMiddleware
from telegram_bot.middlewares.logger_middleware import LoggerMiddleware
from telegram_bot.middlewares.schedule_middleware import SchedulerMiddleware
from telegram_bot.middlewares.user_middleware import UserMiddleware
from utils.config import settings


async def launch_bot() -> None:
    bot = Bot(settings.TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    scheduler = AsyncIOScheduler()
    scheduler.start()
    scheduler.add_job(daily_message, trigger='cron', hour=9, minute=0, kwargs={'bot': bot})
    dp.message.middleware.register(UserMiddleware())
    dp.message.middleware.register(ExceptionMiddleware())
    dp.message.middleware.register(SchedulerMiddleware(scheduler))
    dp.message.middleware.register(LoggerMiddleware())
    dp.include_router(user_router)
    dp.include_router(inline_router)
    dp.include_router(state_router)
    dp.include_router(admin_router)
    dp.include_router(image_router)
    dp.include_router(weather_router)
    dp.include_router(scheduler_router)
    dp.include_router(default_router)
    await set_commands(bot)
    await dp.start_polling(bot)
