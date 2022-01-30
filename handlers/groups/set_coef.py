from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, logger
from filters import IsGroup

from functional.set_coef import set_coef


@logger.catch
@dp.message_handler(IsGroup(), Command("set_coef"))
async def set_coef_handler(message: types.Message):
    args = message.get_args()

    if (args == '' or args.isdigit() == False):
        await message.reply('Введите корректное значение')
        return

    await message.reply(set_coef(message.from_user.id, int(args)))
