from filters import IsAdmin
from functional.update_all_users_puuid import update_all_users_puuid
from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp, logger


@logger.catch
@dp.message_handler(IsAdmin(), Command("update_all_users_puuid"))
async def update_all_users_puuid_handler(message: types.Message):
    await message.answer(await update_all_users_puuid())
