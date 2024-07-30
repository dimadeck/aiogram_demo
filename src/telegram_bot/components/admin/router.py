from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message, BotCommand

from telegram_bot.components.admin.messages import AdminMessages
from telegram_bot.components.user.service import UserService
from telegram_bot.middlewares.admin_middleware import UserNotAdminMiddleware

router = Router()
router.message.middleware(UserNotAdminMiddleware())

commands = [
    BotCommand(command='users', description='Показать пользователей'),
]


@router.message(Command('users'))
async def users_handler(message: Message) -> None:
    users = await UserService().get_all_users()
    await message.answer(AdminMessages.show_users(users))
