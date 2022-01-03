from environs import Env

VERSION = '0.3.0'
CHANGES = f'''Изменения в {VERSION}:
- Добавленна команда /add для добавления подтягиваний
- Добавленна команда /set_coef для установки коэффициента
- Добавленна команда /my_stats для просмотра статистики
- Добавленна команда /history_all для просмотра всей истории
- Добавленна команда /matches_all для просмотра всей истории матчей
- Пофикшен баг с /history и /matches - теперь они выводят 10 последних записей
- update_matches_all больше не выводит пользователей, которые не сыграли игры
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
