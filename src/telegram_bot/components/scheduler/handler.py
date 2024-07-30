from telegram_bot.components.scheduler.messages import ScheduleMessages
from telegram_bot.components.user.service import UserService


async def daily_message(bot):
    users = await UserService().get_all_users()
    for user in users:
        await bot.send_message(user.id, ScheduleMessages.daily_message())


async def remind_user(message, state):
    await message.answer(ScheduleMessages.remind_message())
    await state.clear()

