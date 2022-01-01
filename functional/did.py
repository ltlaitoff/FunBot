import data
from loader import database, logger, dp, api
from datetime import datetime

from functional.add_new_record_in_history import add_new_record_in_history


def did(tg_id, value):
    user_info = database.users.get_by_tg_id(tg_id)
    user_id = user_info.get('id')
    date = datetime.now()
    current_coef = user_info.get('coefficient')
    result_pull_ups = value
    global_pull_ups = user_info.get('pull_ups') - result_pull_ups

    if (global_pull_ups < 0):
        global_pull_ups = 0

    database.history.add(user_id, date, value, current_coef,
                         result_pull_ups, global_pull_ups)
    database.users.update_pull_ups(user_id, global_pull_ups)
    return 'Подтягивания успешно убраны'
