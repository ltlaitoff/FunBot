import data
from loader import database, logger, dp, api
from datetime import datetime

from data.messages_form import my_stats_message


def my_stats(tg_id):
    user_info = database.users.get_by_tg_id(tg_id)
    return my_stats_message(user_info)
