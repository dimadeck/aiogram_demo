import os.path

from aiogram import Router, F
from aiogram.filters.command import Command
from aiogram.types import Message, BotCommand

from telegram_bot.components.image.messages import ImageMessages
from utils.config import settings

router = Router()
commands = [
    BotCommand(command='photo', description='Узнать размер изображения'),
]


@router.message(F.photo, Command('photo'))
async def photo_handler(message: Message, bot) -> None:
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


async def download_photo(bot, photo):
    if not settings.IMAGE_DIR:
        return
    file_info = await bot.get_file(photo.file_id)
    destination = os.path.join(settings.IMAGE_DIR, file_info.file_path)
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    await bot.download_file(file_info.file_path, destination=destination)
    return os.path.exists(destination)
