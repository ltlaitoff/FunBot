from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, database


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(Command("authorization"))
async def authorization(message: types.Message):
    database.add_new_telegram_user(
        message.from_user.id, message.from_user.first_name)
