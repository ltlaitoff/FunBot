from functional.create_new_lol_user import create_new_lol_user
from loader import dp, database, logger
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram import types

from functional.update_user_mathes import update_user_mathes
from filters import IsGroup


@dp.message_handler(IsGroup(), Command("update_matches"))
async def update_matches(message: types.Message):
    await message.answer(update_user_mathes(message.from_user.id))
