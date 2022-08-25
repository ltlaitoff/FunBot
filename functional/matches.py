from loader import database, logger, dp, api
from datetime import datetime
from functional.get_matches_table import get_matches_table

@logger.catch
def matches(tg_id):
    user_info = database.users.get_by_tg_id(tg_id)
    matches_list = database.matchs.get_by_user_id(user_info.get('id'))[::-1][:20]

    if (len(matches_list) == 0):
        return 'Not found'

    return get_matches_table(matches_list, user_info, pull_ups = False, coef = False)
