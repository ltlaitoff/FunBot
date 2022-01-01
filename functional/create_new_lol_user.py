from loader import database, logger
# from api.api import get_user_info

from functional.update_user_mathes import update_user_mathes


def create_new_lol_user(tg_id, text):
    logger.critical('create_new_lol_user')
    # user_info = get_user_info(text)

    # if (user_info.get('status') != None):
    #     return "Вы ввели неверное имя пользователя или произошла ошибка"

    # if (database.get_all_by_tg_id(tg_id) == []):
    #     return "Вас нет в БД. Авторизуйтесь - /authorization"

    # database.update_user_lol_data(
    #     tg_id, user_info.get('puuid'), user_info.get('name'))

    # return update_user_mathes(tg_id) + "\nВаши данные успешно добавленны"
