from loader import database, logger, dp, api

from functional.add_new_record_in_history import add_new_record_in_history


async def update_user_mathes(tg_id, chat_id, return_type='tg'):
    user_info = database.users.get_by_tg_id(tg_id)
    user_id = user_info.get('id')
    puuid = user_info.get('lol_puuid')
    coef = user_info.get('coefficient')
    pull_ups = user_info.get('pull_ups')

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

    if (return_type == 'all'):
        return create_matches_message(matches, return_type, coef, pull_ups)

    await dp.bot.send_message(chat_id, create_matches_message(matches, coef, pull_ups))


def create_matches_message(matches, return_type, coef, pull_ups):
    if (len(matches) == 0):
        return ''

    message = ''
    if (return_type != 'all'):
        message = 'Matches(date, champion, KDA):\n'

    for item in matches:
        message += transfrom_to_send_user(*item, coef, pull_ups)

    return message


def transfrom_to_send_user(date, champion, kills, deaths, assists, coef, pull_ups):
    return f'{date}, {champion} -> {kills} | {deaths} | {assists} => {pull_ups} + {deaths} * {coef} = {pull_ups + deaths * coef}\n'
