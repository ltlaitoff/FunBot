from loader import dp, logger
from aiogram.dispatcher.filters import Command
from aiogram import types

from functional.update_user_mathes import update_user_mathes
from filters import IsGroup


@logger.catch
@dp.message_handler(IsGroup(), Command("update_matches"))
async def update_matches(message: types.Message):
    await update_user_mathes(message.from_user.id, message.chat.id)
