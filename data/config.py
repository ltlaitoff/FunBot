from environs import Env

VERSION = '0.1.0'

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
CHAT = env.str("CHAT")
RIOT_API = env.str("RIOT_API")
RIOT_LOCALE = env.str("RIOT_LOCALE")
