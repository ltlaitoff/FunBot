from loguru import logger
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


@logger.catch
class IsGroup(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type in (types.ChatType.GROUP,
                                     types.ChatType.SUPERGROUP)


@logger.catch
class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE
