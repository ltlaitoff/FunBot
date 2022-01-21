from loader import database, logger, dp, api


@logger.catch
async def update_all_users_puuid():
    users_list = database.users.get_all()

    result_message = ''
    for user in users_list:
        user_lol_name = user.get('lol_name')

        api_user_info = api.get_user_info_by_name(user_lol_name)

        if (api_user_info == None):
            result_message += f'❗️ Не удалось обновить puuid для {user.get("tg_name")} - {user_lol_name}\n'
            continue

        if (database.users.update_lol_puuid(user.get('id'), api_user_info.get('puuid')) == 0):
            result_message += f'✅ Puuid для {user.get("tg_name")} - {user_lol_name} успешно обновленно\n'

    return result_message
