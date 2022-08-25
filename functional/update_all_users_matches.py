from loader import database, logger, dp

from functional.update_user_mathes import update_user_mathes


@logger.catch
async def update_all_users_matches(chat_id, call_type="user"):
    all_users = database.users.get_all()

    for user in all_users:
        await update_user_mathes(user.get("tg_id"), chat_id, 'all')
