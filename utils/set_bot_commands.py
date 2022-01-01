from aiogram import types


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
        ]
    )
