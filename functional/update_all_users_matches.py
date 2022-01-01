from loader import database, logger, dp

from functional.update_user_mathes import update_user_mathes


async def update_all_users_matches(chat_id):
    all_users = database.users.get_all()

    result_arr = []
    for user in all_users:
        result_arr.append(await update_user_mathes(user.get("tg_id"), chat_id, 'all'))

    if (len(result_arr) == 0):
        return

    result = '[ALL_UPDATE] Matches(date, champion, KDA):\n'

    for item in result_arr:
        result += f'{user.get("tg_name")}:\n'
        result += item
        result += '\n\n'

    await dp.bot.send_message(chat_id, result)
