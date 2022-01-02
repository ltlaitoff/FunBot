from loader import dp, database, logger, config
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram import types

from functional.update_user_mathes import update_user_mathes
from filters import IsGroup


@dp.message_handler(IsGroup(), Command("version"))
async def update_matches(message: types.Message):
    await message.answer('Current version: v' + config.VERSION)


@dp.message_handler(IsGroup(), Command("changes"))
async def update_matches(message: types.Message):
    await message.answer(config.CHANGES)
