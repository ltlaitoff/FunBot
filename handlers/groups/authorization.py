from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, logger
from filters import IsGroup

from functional.create_new_user import create_new_user


@logger.catch
@dp.message_handler(IsGroup(), Command("authorization"))
async def authorization(message: types.Message):
    await message.reply(create_new_user(message.from_user.id, message.from_user.first_name))
