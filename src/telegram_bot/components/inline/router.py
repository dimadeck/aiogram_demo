import enum
from typing import Optional

from aiogram import Router
from aiogram.filters.callback_data import CallbackData
from aiogram.filters.command import Command
from aiogram.types import Message, BotCommand, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from telegram_bot.components.inline.messages import InlineMessages

router = Router()
commands = [
    BotCommand(command='show_inline_buttons', description='Показ Inline-кнопок'),
]


class ButtonChoice(enum.Enum):
    first_button: str = 'first_button'
    second_button: str = 'second_button'


class InlineButtonCallback(CallbackData, prefix="inline_callback"):
    data: Optional[str] = None


async def get_keyboard() -> InlineKeyboardBuilder:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text='ℹ️ Выбор 1',
        callback_data=InlineButtonCallback(data=ButtonChoice.first_button).pack()
    )
    keyboard.button(
        text='📦 Выбор 2',
        callback_data=InlineButtonCallback(data=ButtonChoice.second_button).pack()
    )
    keyboard.adjust(2)
    return keyboard


@router.message(Command('show_inline_buttons'))
async def show_inline_buttons(message: Message) -> None:
    keyboard = await get_keyboard()
    await message.answer(InlineMessages.make_choice(), reply_markup=keyboard.as_markup())


@router.callback_query(InlineButtonCallback.filter())
async def check_collect_callback(call: CallbackQuery):
    choice = InlineButtonCallback.unpack(call.data).data
    if choice == ButtonChoice.first_button.value:
        await call.message.answer(InlineMessages.first_button())
    elif choice == ButtonChoice.second_button.value:
        await call.message.answer(InlineMessages.second_button())
    else:
        await call.message.answer(InlineMessages.error_choice())
    await call.answer()
