from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.types import Message, BotCommand

from telegram_bot.components.user.messages import UserMessages
from telegram_bot.components.user.service import UserService

router = Router()

commands = [
    BotCommand(command='start', description='Старт'),
    BotCommand(command='help', description='Помощь'),
    BotCommand(command='me', description='Аккаунт'),
    BotCommand(command='admin_on', description='Включить режим администратора'),
    BotCommand(command='admin_off', description='Отключить режим администратора'),
]


@router.message(CommandStart())
async def command_start_handler(message: Message, user) -> None:
    await message.answer(UserMessages.welcome_message(user))


@router.message(Command('me'))
async def command_start_handler(message: Message, user) -> None:
    await message.answer(UserMessages.me(user))


@router.message(Command('help'))
async def command_start_handler(message: Message) -> None:
    await message.answer(UserMessages.help())


@router.message(Command('admin_on'))
async def admin_on(message: Message, user) -> None:
    user = await UserService().change_admin_role(user.id, True)
    await message.answer(UserMessages.admin_status(user.is_admin))


@router.message(Command('admin_off'))
async def admin_off(message: Message, user) -> None:
    user = await UserService().change_admin_role(user.id, False)
    await message.answer(UserMessages.admin_status(user.is_admin))
