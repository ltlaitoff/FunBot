from loader import database, logger, dp, api
from datetime import datetime


def history(tg_id):
    user_info = database.users.get_by_tg_id(tg_id)
    user_id = user_info.get('id')

    history_list = database.history.get_by_user_id(user_id)

    if (len(history_list) == 0):
        return 'История пустая'

    message = 'История:\n'
    message += 'Дата | Значение | Коофициент | В итоге | Общее\n'
    for item in history_list[:10]:
        message += create_history_string(item) + '\n'

    return message


def create_history_string(item):
    return f'{item.get("date")} | {item.get("value")} | {item.get("current_coef")} | {item.get("result_pull_ups")} | {item.get("global_pull_ups")}'
