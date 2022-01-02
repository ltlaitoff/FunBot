from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, Command

from loader import dp
from filters import IsGroup
from data.messages_form import get_start_message, get_help_message


@dp.message_handler(IsGroup(), CommandHelp())
async def bot_help(message: types.Message):
    await message.answer(get_help_message())


@dp.message_handler(IsGroup(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(get_start_message(message.from_user.full_name))


@dp.message_handler(IsGroup(), Command('message'))
async def bot_start(message: types.Message):
    await message.answer(message)
