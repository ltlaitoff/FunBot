from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from filters import IsGroup


@dp.message_handler(IsGroup(), CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку")

    await message.answer("\n".join(text))


@dp.message_handler(IsGroup(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
