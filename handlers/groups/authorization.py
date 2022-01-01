from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, database
from filters import IsGroup


@dp.message_handler(IsGroup(), Command("authorization"))
async def authorization(message: types.Message):
    database.add_new_telegram_user(
        message.from_user.id, message.from_user.first_name)
