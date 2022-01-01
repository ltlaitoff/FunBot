from loader import dp, database, logger
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram import types

from functional.update_all_users_matches import update_all_users_matches
from filters import IsGroup


@dp.message_handler(IsGroup(), Command("update_all_users_matches"))
async def update_all_users(message: types.Message):
    await update_all_users_matches(message.chat.id)
