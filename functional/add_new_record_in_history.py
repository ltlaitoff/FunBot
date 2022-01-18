from loader import database, logger


def add_new_record_in_history(user_id, date, value, last_global_pull_ups=-1):
    user_info = database.users.get_by_user_id(user_id)

    if (user_info == None):
        logger.critical(f'not find user by user_id {user_id} in database')
        return

    current_coef = user_info.get('coefficient')
    result_pull_ups = value * current_coef

    if (last_global_pull_ups != -1):
        user_pull_ups = last_global_pull_ups
    else:
        user_pull_ups = user_info.get('pull_ups')

    global_pull_ups = user_pull_ups + result_pull_ups

    database.history.add(
        user_id, date, value, current_coef, result_pull_ups, global_pull_ups)

    database.users.update_pull_ups(user_id, global_pull_ups)

    return global_pull_ups
