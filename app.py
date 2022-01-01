from aiogram import executor
import asyncio

from loader import dp, config
import middlewares
import filters
import handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from functional.update_all_users_matches import update_all_users_matches


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


async def update_all_users_matches_loop():
    while True:
        await asyncio.sleep(180)
        await update_all_users_matches(config.CHAT, 'loop')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(update_all_users_matches_loop())
    executor.start_polling(dp, on_startup=on_startup)
