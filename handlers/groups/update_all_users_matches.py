from functional.create_new_lol_user import create_new_lol_user
from loader import dp, database, logger
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram import types

from functional.update_all_users_matches import update_all_users_matches


@dp.message_handler(Command("update_all_users_matches"))
async def update_all_users(message: types.Message):
    await message.answer(update_all_users_matches())
