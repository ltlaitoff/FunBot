from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, database, logger
from filters import IsGroup

from functional.pull_ups_controller import pull_ups_controller

def checkOnNumber(value):
    try:
        int(value)
        return True
    except:
        return False 

@dp.message_handler(IsGroup(), Command("did"))
async def did_handler(message: types.Message):
    args = message.get_args()
    if (args == '' or checkOnNumber(args) == False):
        await message.reply('Введите корректное значение')
        return

    await message.answer(pull_ups_controller(message.from_user.id, int(args), 'did'))
