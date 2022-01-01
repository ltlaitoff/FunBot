from loader import database, logger
from api.api import get_user_matchs_list, get_match_info


def add_new_record_in_history(user_id, data, value):
    user_info = database.get_all_by_user_id(user_id)
    current_coef = user_info[0][6]
    result_pull_ups = value * current_coef
    global_pull_ups = user_info[0][5] + result_pull_ups

    database.add_new_record_in_history(
        user_id, data, value, current_coef, result_pull_ups, global_pull_ups)
    database.update_user_pull_ups(user_id, global_pull_ups)
