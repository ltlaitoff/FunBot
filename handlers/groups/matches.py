from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, database, logger
from filters import IsGroup

from functional.matches import matches


@dp.message_handler(IsGroup(), Command("matches"))
async def matches_handler(message: types.Message):
    await message.answer(matches(message.from_user.id))
