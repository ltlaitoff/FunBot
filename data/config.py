from environs import Env

DEV = False

VERSION = '1.0.0'
CHANGES = f'''- Измененны таблички обновления вывода истории матчей'''

env = Env()
env.read_env()


if (DEV):
    BOT_TOKEN = env.str("BOT_TOKEN_DEV")
    CHAT = env.str("CHAT_DEV")
else:
    BOT_TOKEN = env.str("BOT_TOKEN")
    CHAT = env.str("CHAT")

ADMINS = env.list("ADMINS")
IP = env.str("ip")
RIOT_API = env.str("RIOT_API")
RIOT_LOCALE = env.str("RIOT_LOCALE")

DATE_FORMAT = "%d.%m.%y %H:%M"
