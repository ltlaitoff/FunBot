from loader import dp, logger, config
from aiogram.dispatcher.filters import Command
from aiogram import types

from filters import IsGroup


@logger.catch
@dp.message_handler(IsGroup(), Command("version"))
async def update_matches(message: types.Message):
    await message.answer('Current version: v' + config.VERSION)


@logger.catch
@dp.message_handler(IsGroup(), Command("changes"))
async def update_matches(message: types.Message):
    await message.answer(config.CHANGES)
