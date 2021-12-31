import requests

API_KEY = 'RGAPI-130d88f5-b1d5-4d5e-894f-0efd49a20fb1'
LOCALE = 'europe'


def get_user_info(name):
    return requests.get(f'https://ru.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={API_KEY}').json()


# def get_match_info(match_id):
#     return requests.get(f'https://{LOCALE}.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={API_KEY}').json()


# def add_new_user(name):
#     user = get_user_info(name)
#     database.add_new_user(user['puuid'], user['name'])


# def update_users_last_matches():
#     users = database.get_all_users()
#     for item in users:
#         puuid = item[1]
#         response = requests.get(
#             f'https://{LOCALE}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=40&api_key={API_KEY}').json()

#         if (item[3] != response[0]):
#             for math in get_match_info(response[0])['info']['participants']:
#                 if math['puuid'] == puuid:
#                     print(f"""
#             Lane: {math['lane']}
#             ChampionName: {math['championName']}
#             Kills: {math['kills']}
#             Deaths: {math['deaths']}
#             Assists: {math['assists']}
#           """)
#             database.update_user_last_match(puuid, response[0])


# update_users_last_matches()
