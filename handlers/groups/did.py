from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, logger
from filters import IsGroup

from functional.pull_ups_controller import pull_ups_controller


@logger.catch
@dp.message_handler(IsGroup(), Command("did"))
async def did_handler(message: types.Message):
    args = message.get_args()

    await message.reply(pull_ups_controller(message.from_user.id, args, 'did'))
