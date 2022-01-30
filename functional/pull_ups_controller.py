import data
from loader import database, logger, dp, api
from datetime import datetime

from functional.add_new_record_in_history import add_new_record_in_history


@logger.catch
def input_validation(value, current_command_type):
    if (value >= 0):
        return [value, current_command_type]

    value_abs = abs(value)
    change_ways = {
        'did': 'add',
        'add': 'did'
    }

    return [value_abs, change_ways[current_command_type]]


@logger.catch
def checkOnNumber(value):
    try:
        int(value)
        return True
    except:
        return False


@logger.catch
def pull_ups_controller(tg_id, args, command_type):
    if (checkOnNumber(args) == False):
        return 'Введите корректное значение'

    value, command_type = input_validation(int(args), command_type)

    user_info = database.users.get_by_tg_id(tg_id)
    user_id = user_info.get('id')
    date = datetime.now()
    current_coef = user_info.get('coefficient')
    result_pull_ups = value

    if (command_type == 'did'):
        global_pull_ups = user_info.get('pull_ups') - result_pull_ups
    elif (command_type == 'add'):
        global_pull_ups = user_info.get('pull_ups') + result_pull_ups

    database.history.add(user_id, date, value, current_coef,
                         result_pull_ups, global_pull_ups, f'USER_{command_type.upper()}')
    database.users.update_pull_ups(user_id, global_pull_ups)

    return f'Подтягивания успешно { "убраны" if (command_type == "did") else "добавленны"}\nТекущее количество подтягиваний: {global_pull_ups}'
