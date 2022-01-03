from loader import database, logger, dp, api


def set_coef(tg_id, value):
    user_info = database.users.get_by_tg_id(tg_id)
    user_id = user_info.get('id')
    current_coef = user_info.get('coefficient')

    if (value == current_coef):
        return f'Коофициент уже установлен на {value}'

    if (database.users.update_coefficient(user_id, value) == 0):
        return f'Коофициент установлен на {value}'

    return 'Произошла ошибка, обратитесь к администратору'
