from re import purge
from loader import database, logger, dp, api

# from functional.parse_data_from_match_info import parse_data_from_match_info
from functional.add_new_record_in_history import add_new_record_in_history


async def update_user_mathes(tg_id, chat_id):
    user_info = database.users.get_by_tg_id(tg_id)
    user_id = user_info.get('id')
    puuid = user_info.get('lol_puuid')

    user_database_mathes = database.matchs.get_by_user_id(user_id)
    user_api_mathes = api.get_user_matchs_list(puuid)

    if (user_database_mathes != None):
        last_match_id = user_database_mathes[-1].get('match_id')
    else:
        last_match_id = user_api_mathes[1]

    matches = []

    for match_id in user_api_mathes:
        if (match_id == last_match_id):
            break

        match_data = api.get_match_info(match_id, puuid)
        database.matchs.add(user_id, match_id, *match_data.values())

        add_new_record_in_history(
            user_id, match_data.get('date'), match_data.get('deaths'))

        matches.append([*match_data.values()])

    await send_matches_message(chat_id, matches)


async def send_matches_message(chat_id, matches):
    if (len(matches) == 0):
        return None

    message = 'Matches(date, champion, KDA):\n'
    for item in matches:
        message += transfrom_to_send_user(*item)

    await dp.bot.send_message(chat_id, message)


def transfrom_to_send_user(date, champion, kills, deaths, assists):
    return f'{date}, {champion} -> {kills} | {deaths} | {assists}\n'
