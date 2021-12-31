from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, database, logger

from functional.create_new_lol_user import create_new_lol_user


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(Command("connect_lol"))
async def connect_lol(message: types.Message):
    await message.answer(create_new_lol_user(message.from_user.id, message.get_args()))
