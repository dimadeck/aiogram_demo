from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message, BotCommand

from core.weather.weather import Weather
from telegram_bot.components.weather.messages import WeatherMessages
from utils.config import settings

router = Router()

commands = [
    BotCommand(command='weather', description='Погода'),
]


@router.message(Command('weather'))
async def weather_handler(message: Message) -> None:
    city = message.text.replace('/weather ', '')
    weather = Weather(settings.WEATHER_API_KEY).get_temperature(city)
    await message.answer(WeatherMessages.show_temperature(city, weather))
