from loader import dp, logger
from aiogram.dispatcher.filters import Command
from aiogram import types

from functional.update_all_users_matches import update_all_users_matches
from filters import IsGroup


@logger.catch
@dp.message_handler(IsGroup(), Command("update_all_users_matches"))
async def update_all_users(message: types.Message):
    await update_all_users_matches(message.chat.id)
