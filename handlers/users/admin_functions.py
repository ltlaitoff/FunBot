from loader import dp, logger, config, bot
from aiogram.dispatcher.filters import Command
from aiogram import types
from filters import IsAdmin


@logger.catch
@dp.message_handler(IsAdmin(), Command("admin_commands"))
async def update_matches(message: types.Message):
    await message.reply('Admin commands:\n' +
                        '/send_changes - Отправить сообщение об изменениях\n' +
                        '/database_backup - Скачать бэкап базы данных\n' + 
                        '/message_info - Информация о сообщении')


@logger.catch
@dp.message_handler(IsAdmin(), Command("send_changes"))
async def update_matches(message: types.Message):
    await bot.send_message(config.CHAT,
                           f'Изменения в {config.VERSION}:\n' +
                           f'{config.CHANGES}')


@logger.catch
@dp.message_handler(IsAdmin(), Command("database_backup"))
async def update_matches(message: types.Message):
    with open('utils/db_api/db.db', 'rb') as database_file:
        contents = database_file.read()
        await bot.send_document(config.CHAT, contents, caption='database')

@logger.catch
@dp.message_handler(IsAdmin(), Command("message_info"))
async def update_matches(message: types.Message):
    await message.reply(message)
