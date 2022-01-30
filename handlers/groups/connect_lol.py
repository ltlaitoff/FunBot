from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, logger
from filters import IsGroup

from functional.connect_lol_account import connect_lol_account


@logger.catch
@dp.message_handler(IsGroup(), Command("connect_lol"))
async def connect_lol(message: types.Message):
    await message.answer(connect_lol_account(message.from_user.id, message.get_args()))
