from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, logger
from filters import IsGroup

from functional.history import history


@logger.catch
@dp.message_handler(IsGroup(), Command("history"))
async def history_handler(message: types.Message):
    await message.answer(history(message.from_user.id))


@logger.catch
@dp.message_handler(IsGroup(), Command("history_all"))
async def history_handler(message: types.Message):
    await message.answer(history(message.from_user.id, 'all'))
