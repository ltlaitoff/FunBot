from loader import database, logger


def create_new_user(tg_id, tg_name):
    user = database.users.get_by_tg_id(tg_id)

    if (user != None):
        return 'Вы уже находитесь в базе'

    if (database.users.add(tg_id=tg_id, tg_name=tg_name) == 0):
        return 'Вы были успешно добавленны'

    return 'Что-то пошло не так, обратитесь к администратору'
