from loader import database, logger, dp

from functional.update_user_mathes import update_user_mathes


async def update_all_users_matches(chat_id):
    all_users = database.users.get_all()

    result = '[ALL_UPDATE] Matches(date, champion, KDA):\n'
    for user in all_users:
        result += f'{user.get("tg_name")}:\n'
        result += await update_user_mathes(user.get("tg_id"), chat_id, 'all')
        result += '\n\n'

    await dp.bot.send_message(chat_id, result)
