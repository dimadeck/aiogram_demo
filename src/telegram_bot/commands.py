from aiogram import Bot

from telegram_bot.components.admin.router import commands as admin_commands
from telegram_bot.components.base.router import commands as default_commands
from telegram_bot.components.image.router import commands as image_commands
from telegram_bot.components.inline.router import commands as inline_commands
from telegram_bot.components.scheduler.router import commands as scheduler_commands
from telegram_bot.components.state.router import commands as state_commands
from telegram_bot.components.user.router import commands as user_commands
from telegram_bot.components.weather.router import commands as weather_commands


async def set_commands(bot: Bot):
    commands = default_commands + user_commands + inline_commands + state_commands + \
               admin_commands + image_commands + weather_commands + scheduler_commands
    await bot.set_my_commands(commands)
