import datetime

from aiogram import Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, BotCommand

from telegram_bot.components.scheduler.handler import remind_user
from telegram_bot.components.scheduler.messages import ScheduleMessages

router = Router()
commands = [
    BotCommand(command='remind_me', description='Написать через 15 минут'),
]


@router.message(Command('remind_me'))
async def remind_me(message: Message, user, scheduler, state: FSMContext) -> None:
    job = scheduler.add_job(
        remind_user,
        trigger='date',
        run_date=datetime.datetime.now() + datetime.timedelta(minutes=15),
        kwargs=dict(message=message, state=state)
    )
    await state.set_state(WaitingStates.WAITING_ANSWER)
    await state.update_data(job_id=job.id)
    await message.answer(ScheduleMessages.welcome_message(username=user.name))


class WaitingStates(StatesGroup):
    WAITING_ANSWER = State()


@router.message(WaitingStates.WAITING_ANSWER)
async def cancel_task(message: Message, state: FSMContext, scheduler):
    await message.answer(ScheduleMessages.cancel_waiting())
    data = await state.get_data()
    scheduler.remove_job(data['job_id'])
    await state.clear()
