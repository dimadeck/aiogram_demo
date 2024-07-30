from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, BotCommand

from telegram_bot.components.state.messages import StateMessages
from telegram_bot.components.user.schema import UserSchema

router = Router()
commands = [
    BotCommand(command='state_routine', description='Запуск анкеты'),
]


class BasicStates(StatesGroup):
    WAIT_NAME = State()
    WAIT_AGE = State()


@router.message(Command('state_routine'))
async def launch_state_routine(message: Message, state: FSMContext, user: UserSchema) -> None:
    await state.set_state(BasicStates.WAIT_NAME)
    await message.answer(StateMessages.wait_name_message(user))


@router.message(BasicStates.WAIT_NAME)
async def wait_name_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(BasicStates.WAIT_AGE)
    await message.answer(StateMessages.wait_age_message())


@router.message(BasicStates.WAIT_AGE)
async def wait_age_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(age=int(message.text))
    user_data = await state.get_data()
    await message.answer(
        StateMessages.show_info_message(
            user_data['name'],
            user_data['age']
        )
    )
    await state.clear()
