import os.path
from typing import Optional

from aiogram import Router, Bot
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, BotCommand, PhotoSize

from telegram_bot.components.image.messages import ImageMessages
from utils.config import settings

router = Router()
commands = [
    BotCommand(command='photo', description='Узнать размер изображения'),
]


class PhotoStates(StatesGroup):
    WAIT_PHOTO = State()


@router.message(Command('photo'))
async def photo_handler(message: Message, bot: Bot, state: FSMContext) -> None:
    if message.photo:
        await photo_routine(message, bot)
        return
    await state.set_state(PhotoStates.WAIT_PHOTO)
    await message.answer(ImageMessages.need_photo())


@router.message(PhotoStates.WAIT_PHOTO)
async def wait_photo_handler(message: Message, bot: Bot, state: FSMContext) -> None:
    if message.photo:
        await state.clear()
        await photo_routine(message, bot)
        return


async def photo_routine(message, bot):
    photo = message.photo[-1]
    downloaded = await download_photo(bot, photo)
    await message.answer(
        ImageMessages.photo_info(
            size=photo.file_size,
            width=photo.width,
            height=photo.height,
            downloaded=downloaded
        )
    )


async def download_photo(bot: Bot, photo: PhotoSize) -> Optional[bool]:
    if not settings.IMAGE_DIR:
        return
    file_info = await bot.get_file(photo.file_id)
    destination_path = os.path.join(settings.IMAGE_DIR, file_info.file_path)
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    await bot.download_file(file_info.file_path, destination=destination_path)
    return os.path.exists(destination_path)
