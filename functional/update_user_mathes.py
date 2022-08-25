from loader import database, logger, dp, api

from functional.add_new_record_in_history import add_new_record_in_history
from functional.get_matches_table import get_matches_table
from prettytable import PrettyTable

@logger.catch
def getUserLastMatch(user_id, api_last_match_id):
    user_database_mathes = database.matchs.get_by_user_id(user_id)

    if (user_database_mathes != None):
        return user_database_mathes[-1].get('match_id')
    return api_last_match_id


@logger.catch
async def update_user_mathes(tg_id, chat_id, return_type='tg'):
    user_info = database.users.get_by_tg_id(tg_id)
    user_id = user_info.get('id')
    puuid = user_info.get('lol_puuid')
    coef = user_info.get('coefficient')

    user_api_mathes = api.get_user_matchs_list(puuid)
    last_match_id = getUserLastMatch(user_id, user_api_mathes[len(user_api_mathes) - 1])

    matches = []

    last_match_index = user_api_mathes.index(last_match_id)
    new_matches = user_api_mathes[:last_match_index][::-1]
    last_global_pull_ups = user_info.get('pull_ups')

    for match_id in new_matches:
        match_data = api.get_match_info(match_id, puuid)
        
        database.matchs.add(user_id, match_id, match_data)

        match_data['pull_ups'] = add_new_record_in_history(
            user_id, match_data.get('date'), match_data.get('deaths'), last_global_pull_ups)

        last_global_pull_ups = match_data['pull_ups']

        matches.append(match_data)

    table = get_matches_table(matches, user_info)
    
    if (table == ''):
        if (return_type == 'all'):
            return

        await dp.bot.send_message(chat_id, 'Matches not found')
        return

    await dp.bot.send_message(chat_id, f'```\n{table}```', parse_mode="MarkdownV2")
