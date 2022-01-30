from environs import Env

DEV = False

VERSION = '0.3.1'
CHANGES = f'''Изменения в {VERSION}:
- Добавленна поддержка нового API ключа
- Исправленны некоторые баги
'''

env = Env()
env.read_env()


if (DEV):
  BOT_TOKEN = env.str("BOT_TOKEN_DEV")
else:
  BOT_TOKEN = env.str("BOT_TOKEN")

ADMINS = env.list("ADMINS")
IP = env.str("ip")
CHAT = env.str("CHAT")
RIOT_API = env.str("RIOT_API")
RIOT_LOCALE = env.str("RIOT_LOCALE")

DATE_FORMAT = "%d.%m.%y %H:%M"
