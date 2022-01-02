from loader import config


def get_start_message(full_name):
    return f'Привет, {full_name}!\nТекущая версия бота: {config.VERSION}'


def get_help_message():
    text = ("/start - Запустить бота",
            "/help - Вывести справку",
            "/authorization - Зарегистрироватся в боте",
            "/connect_lol - connect_lol {name} Присоединить lol аккаунт",
            "/update_all_users_matches - Обновить матчи всех пользователей",
            "/update_matches - Обновить свои матчи",
            "/history - Посмотреть историю",
            "/matches - Посмотреть матчи",
            "/show_pull_ups - Посмотреть подтягивания",
            "/version - Текущая версия бота"
            )
    return "\n".join(text)
