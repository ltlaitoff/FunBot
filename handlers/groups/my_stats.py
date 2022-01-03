from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, database
from filters import IsGroup

from functional.my_stats import my_stats


@dp.message_handler(IsGroup(), Command("my_stats"))
async def my_stats_handler(message: types.Message):
    await message.reply(my_stats(message.from_user.id))
