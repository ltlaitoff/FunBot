import requests
from loguru import logger
from datetime import datetime


class RIOT_API:
    @logger.catch
    def __init__(self, config):
        self.config = config
        self.API_KEY = self.config.RIOT_API
        self.LOCALE = self.config.RIOT_LOCALE

    @logger.catch
    def get_user_info_by_name(self, name):
        user_info = requests.get(
            f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={self.API_KEY}').json()

        if (user_info.get('status') != None):
            return None

        return user_info

    @logger.catch
    def get_user_matchs_list(self, puuid):
        return requests.get(
            f'https://{self.LOCALE}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=100&api_key={self.API_KEY}').json()

    @logger.catch
    def get_match_info(self, match_id, puuid):
        return self.__match_info_structuring(
            requests.get(
                f'https://{self.LOCALE}.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={self.API_KEY}').json(),
            puuid
        )

    @logger.catch
    def __match_info_structuring(self, math_json, puuid):
        result = {}
        result["date"] = datetime.fromtimestamp(math_json['info']['gameCreation'] / 1000).strftime(
            self.config.DATE_FORMAT)


        result['queueId'] = math_json['info']['queueId']

        for item in math_json['info']['participants']:
            if (item['puuid'] == puuid):
                result["champion"] = item["championName"]
                result["kills"] = item["kills"]
                result["deaths"] = item["deaths"]
                result["assists"] = item["assists"]
                result["teamPosition"] = item["teamPosition"]
                result["win"] = item["win"]

        return result
