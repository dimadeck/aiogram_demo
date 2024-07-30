from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message, BotCommand

router = Router()
commands = [
    BotCommand(command='echo', description='Эхо-тест'),
]


@router.message(Command('echo'))
async def echo_handler(message: Message) -> None:
    await message.answer(message.text.replace('/echo ', ''))


@router.message()
async def unknown_handler(message: Message) -> None:
    raise ValueError('Unknown message')
