from datetime import datetime


def parse_data_from_match_info(math_json, puuid):
    result = {}
    result["date"] = datetime.fromtimestamp(math_json['info']['gameCreation'] / 1000).strftime(
        "%A, %B %d, %Y %I:%M:%S")

    for item in math_json['info']['participants']:
        if (item['puuid'] == puuid):
            result["champion"] = item["championName"]
            result["kills"] = item["kills"]
            result["deaths"] = item["deaths"]
            result["assists"] = item["assists"]

    return result
