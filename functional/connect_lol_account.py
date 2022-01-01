from loader import database, logger, api

from functional.update_user_mathes import update_user_mathes


def connect_lol_account(tg_id, text):
    user = database.users.get_by_tg_id(tg_id)

    if (user == None):
        return 'Вас нет в базе. Сначала введите /authorization'

    user_id = user.get('id')

    user_info = api.get_user_info_by_name(text)

    if (user_info == None):
        return "Вы ввели неверное имя пользователя или произошла ошибка"

    if (
        (database.users.update_lol_puuid(user_id, user_info.get('puuid')) == 0) and
        (database.users.update_lol_name(user_id, user_info.get('name')) == 0)
    ):
        return 'Данные были успешно обновленны'

    return 'Произошла ошибка, обратитесь к администратору'
