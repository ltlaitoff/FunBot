from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, logger
from filters import IsGroup

from functional.show_pull_ups import show_pull_ups


@logger.catch
@dp.message_handler(IsGroup(), Command("show_pull_ups"))
async def show_pull_ups_handler(message: types.Message):
    await message.answer(show_pull_ups())
