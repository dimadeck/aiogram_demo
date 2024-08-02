from aiogram import Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, BotCommand

from core.weather.weather import Weather
from telegram_bot.components.weather.messages import WeatherMessages
from utils.config import settings

router = Router()

commands = [
    BotCommand(command='weather', description='Погода'),
]


class WeatherStates(StatesGroup):
    WAIT_WEATHER = State()


@router.message(Command('weather'))
async def weather_handler(message: Message, state: FSMContext) -> None:
    city = message.text.replace('/weather', '').strip()
    if not city:
        await message.answer(WeatherMessages.wait_city())
        await state.set_state(WeatherStates.WAIT_WEATHER)
        return
    await check_weather(city, message)


async def check_weather(city: str, message: Message) -> None:
    weather = Weather(settings.WEATHER_API_KEY).get_temperature(city)
    await message.answer(WeatherMessages.show_temperature(city, weather))


@router.message(WeatherStates.WAIT_WEATHER)
async def wait_weather_handler(message: Message, state: FSMContext) -> None:
    await state.clear()
    city = message.text.strip()
    await check_weather(city, message)
