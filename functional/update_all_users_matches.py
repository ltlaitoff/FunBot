from loader import database, logger, dp

from functional.update_user_mathes import update_user_mathes


@logger.catch
async def update_all_users_matches(chat_id, call_type="user"):
    all_users = database.users.get_all()

    result_arr_names = []
    result_arr_text = []
    for user in all_users:
        result_arr_names.append(user.get("tg_name"))
        result_arr_text.append(await update_user_mathes(user.get("tg_id"), chat_id, 'all'))

    if (check_array_on_void(result_arr_text) == True and call_type != "user"):
        return

    result = '[ALL_UPDATE] Matches(date, champion, KDA):\n'

    for index in range(len(result_arr_text)):
        if (result_arr_text[index] != ''):
            result += f'{result_arr_names[index]}:\n'
            result += result_arr_text[index]
            result += '\n'

    await dp.bot.send_message(chat_id, result)


@logger.catch
def check_array_on_void(arr):
    for i in arr:
        if i != '':
            return False

    return True
