from loader import database, logger, dp, api
from datetime import datetime


@logger.catch
def matches(tg_id, message_type='standart'):
    user_info = database.users.get_by_tg_id(tg_id)
    user_id = user_info.get('id')

    matches_list = database.matchs.get_by_user_id(user_id)

    if (len(matches_list) == 0):
        return 'История каток пустая'

    message = 'История каток:\n'
    message += 'Дата | Чемпион | Килы | Смерти | Ассисты\n'

    if (message_type == 'all'):
        arr_on_message = matches_list
    else:
        arr_on_message = matches_list[::-1][:10][::-1]

    for item in arr_on_message:
        message += create_matches_string(item) + '\n'

    return message


@logger.catch
def create_matches_string(item):
    return f'{item.get("date")} | {item.get("champion")} | {item.get("kills")} | {item.get("deaths")} | {item.get("assists")}'
