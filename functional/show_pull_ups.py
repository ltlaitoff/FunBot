import data
from loader import database, logger, dp, api


@logger.catch
def show_pull_ups():
    users = database.users.get_all()
    message = ''

    for user in users:
        message += f'{user.get("tg_name")}: {user.get("pull_ups")}\n'

    return message
