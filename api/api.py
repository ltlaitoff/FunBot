import requests
from data.config import config


class RIOT_API:
    def __init__(self):
        self.API_KEY = config.RIOT_API
        self.LOCALE = config.RIOT_LOCALE

    def get_user_info_by_name(self, name):
        return requests.get(f'https://ru.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={self.API_KEY}').json()

    def get_user_matchs_list(self, puuid):
        return requests.get(
            f'https://{self.LOCALE}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=50&api_key={self.API_KEY}').json()

    def get_match_info(self, match_id):
        return requests.get(f'https://{self.LOCALE}.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={self.API_KEY}').json()
