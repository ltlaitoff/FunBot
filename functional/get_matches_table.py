from loader import database, logger, dp, api
from prettytable import PrettyTable
from data import config
from datetime import datetime

@logger.catch
def getGameType(queueId):
    gameTypes = {
        400: 'Normal',
        420: 'SRanks',
        440: 'GRanks',
        450: 'ARAM',
        1400: 'Book'
    }

    try:
        return gameTypes[queueId]
    except KeyError as e:
        return 'UNSUPPORTED'

@logger.catch
def getWin(win):
    if (win): return 'W'
    return 'L'

@logger.catch
def get_matches_table(matches, user_info, pull_ups = True, coef = True):
    if (len(matches) == 0):
        return ''
    
    params = ['Date', 'Game', '', 'Role', 'Champ', 'K', 'D', 'A']
    if (coef): params.append('Coef')
    if (pull_ups): params.append('Pull ups')

    message = f'  {user_info["lol_name"]}\n'
    for match in matches:
        gameType = getGameType(match['queueId'])
        win = getWin(match['win'])  
        

        date = ''
        if (type(match['date']) == str):
            date = datetime.strptime(match['date'], config.DATE_FORMAT).strftime('%d-%m')
        else:
            date = match['date'].strftime('%d/%m')
            
            
        message += f'''{date} [{win}] {gameType}, {match['champion']}: {match['kills']} | {match['deaths']} | {match['assists']}'''

        if pull_ups: message += f''' => {match["pull_ups"]}(+{match["deaths"]} * {user_info.get('coefficient')})'''

        message += '\n'

    return message

