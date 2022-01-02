from environs import Env

VERSION = '0.2.0'
CHANGES = f'''Изменения в {VERSION}:
- Добавленна проверка на число в /did
- Измененно отображение истории(добавленна более удобная форма просмотра данных от пользователя и от игр)
- Измененно отображение all updates(добавленны подтягивания)
- Исправленны некоторые баги
'''

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
CHAT = env.str("CHAT")
RIOT_API = env.str("RIOT_API")
RIOT_LOCALE = env.str("RIOT_LOCALE")

DATE_FORMAT = "%d.%m.%y %H:%M"
