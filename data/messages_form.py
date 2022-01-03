from loader import config, logger


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


def get_history_message(history_list):
    def __create_history_string(item):
        date = item.get("date").strftime(config.DATE_FORMAT)
        record_type = item.get('record_type')
        value = item.get("value")
        coef = item.get("current_coef")
        result_pull_ups = item.get("result_pull_ups")
        global_pull_ups = item.get("global_pull_ups")

        if (record_type == "GAME"):
            return f'GAME | {date} | {value} * {coef} = {global_pull_ups - value * coef} + {result_pull_ups} = {global_pull_ups}'
        if (record_type == "USER"):
            return f'USER | {date} | {global_pull_ups + value} - {value} = {global_pull_ups}'

    if (len(history_list) == 0):
        return 'История пустая'

    message = 'История:\n'
    message += 'Тип | Дата | Смерти * coef + pull_ups_old = pull_ups\n'

    for item in history_list[:10]:
        message += __create_history_string(item) + '\n'

    return message


def my_stats_message(user_info):
    text = (
        f"Tg name: {user_info.get('tg_name')}\n"
        f"Lol name: {user_info.get('lol_name')}\n"
        f"Pull ups: {user_info.get('pull_ups')}\n"
        f"Coef: {user_info.get('coefficient')}"
    )

    return text
