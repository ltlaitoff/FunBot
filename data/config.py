from environs import Env

DEV = True

VERSION = '0.3.2'
CHANGES = f'''- Изменён функционал did и add. Теперь при did -1 будет выполнятся add 1
- Добавленны команды администратора
- Добавленны бэкапы базы данных
- Fix bugs'''

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
