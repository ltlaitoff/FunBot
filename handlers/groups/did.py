from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, database, logger
from filters import IsGroup

from functional.did import did


@dp.message_handler(IsGroup(), Command("did"))
async def did_handler(message: types.Message):
    args = message.get_args()
    if (args == ''):
        await message.reply('Введите корректное значение')
        return

    await message.answer(did(message.from_user.id, int(args)))
