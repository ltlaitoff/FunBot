from loguru import logger
from aiogram import types


@logger.catch
async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("authorization", "Зарегистрироватся в боте"),
            types.BotCommand(
                "connect_lol", "connect_lol {name} Присоединить lol аккаунт"),
            types.BotCommand("update_all_users_matches",
                             "Обновить матчи всех пользователей"),
            types.BotCommand("update_matches", "Обновить свои матчи"),
            types.BotCommand("history", "Посмотреть историю"),
            types.BotCommand("matches", "Посмотреть матчи"),
            types.BotCommand("show_pull_ups", "Посмотреть подтягивания"),
            types.BotCommand("version", "Текущая версия бота"),
            types.BotCommand("add", "Добавить подтягивания"),
            types.BotCommand("history_all", "Полная история"),
            types.BotCommand("matches_all", "Полная история матчей"),
            types.BotCommand("set_coef", "Установка коофициента"),
            types.BotCommand("my_stats", "Просмотр статистики"),
            types.BotCommand("admin_commands", 'Команды администратора')

        ]
    )
