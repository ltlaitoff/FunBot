from loguru import logger

from aiogram import Dispatcher

from data.config import ADMINS


@logger.catch
async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logger.error(err)
