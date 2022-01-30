from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, database, logger
from filters import IsGroup

from functional.pull_ups_controller import pull_ups_controller


@dp.message_handler(IsGroup(), Command("add"))
async def add_handler(message: types.Message):
    args = message.get_args()
    
    await message.answer(pull_ups_controller(message.from_user.id, args, 'add'))
