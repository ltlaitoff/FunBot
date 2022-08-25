from loader import database, logger, dp, api
from prettytable import PrettyTable

@logger.catch
def getGameType(queueId):
    gameTypes = {
        400: 'Normal Draft',
        420: 'Ranked Solo',
        440: 'Ranked Flex',
        450: 'ARAM',
        1400: 'Spellbook'
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

    table = PrettyTable(params)

    table.title = user_info['lol_name']

    table.align['K'] = 'r'
    table.align['D'] = 'r'
    table.align['A'] = 'r'
    table.align['Champ'] = 'l'
    table.align['Role'] = 'l'
    table.align['Game'] = 'l'

    for match in matches:
        gameType = getGameType(match['queueId'])
        win = getWin(match['win'])  

        data = [match['date'], gameType, win, match['teamPosition'], match['champion'], match['kills'], match['deaths'], match['assists']]

        if coef: data.append(user_info['coefficient'])
        if pull_ups: data.append(f'{match["pull_ups"]}(+{match["deaths"]})')

        table.add_row(data)

    return table

