from loader import database, logger, dp
from api.api import get_user_matchs_list, get_match_info

from functional.parse_data_from_match_info import parse_data_from_match_info
from functional.add_new_record_in_history import add_new_record_in_history


def update_user_mathes(tg_id):
    user_info = database.get_all_by_tg_id(tg_id)[0]
    user_id = user_info[0]
    puuid = user_info[3]
    last_match_id = database.get_last_user_match(user_id)

    match_list = get_user_matchs_list(puuid)

    array_on_send_user = []
    if (last_match_id == []):
        match_data = get_match_info(match_list[0])
        match_structuring_data = parse_data_from_match_info(match_data, puuid)
        database.add_new_match(
            user_id, match_list[0], *match_structuring_data.values())
        array_on_send_user.append(list(match_structuring_data.values()))

    result = []
    for match_id in match_list:
        if (match_id == last_match_id[-1][0]):
            break

        match_data = get_match_info(match_id)
        match_structuring_data = parse_data_from_match_info(match_data, puuid)

        result.append([user_id, match_id, *
                      match_structuring_data.values()])
        array_on_send_user.append(list(match_structuring_data.values()))

    result.reverse()

    for item in result:
        database.add_new_match(*item)
        add_new_record_in_history(user_id, item[2], item[5])

    print(array_on_send_user)

    if (array_on_send_user != []):
        send_result(array_on_send_user)

    return ''


async def send_result(array_on_send_user):
    result = '''Matches:\n'''
    for item in array_on_send_user:
        result += f'''{item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]}\n'''

    await dp.bot.send_message(906687130, "Бот Запущен")
