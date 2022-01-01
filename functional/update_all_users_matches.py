from loader import database, logger, bot

from functional.update_user_mathes import update_user_mathes


def update_all_users_matches():
    logger.critical('update_all_users_matches')
    # all_users = database.get_all_users()
    # print(all_users)

    # result = ''
    # for user in all_users:
    #     result += f'{user[2]}:\n'
    #     result += update_user_mathes(user[1])
    #     result += '\n'

    # return result
