from loader import database, logger, dp, api
from datetime import datetime

from data.messages_form import get_history_message


def history(tg_id, type_message='standart'):
    user_info = database.users.get_by_tg_id(tg_id)
    user_id = user_info.get('id')

    history_list = database.history.get_by_user_id(user_id)

    if (len(history_list) == 0):
        return 'История пустая'

    if (type_message == 'all'):
        return get_history_message(history_list)

    return get_history_message(history_list[::-1][:10][::-1])
