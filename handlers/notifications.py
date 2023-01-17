import time
import logging
from aiogram import Bot, types

from dispatcher import dp, bot

@dp.message_handler(commands=["start"])
async def process_start_cmd(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply(f'Привет, {user_full_name}!'
                        '\nЭто бот модератор'
                        '\nЧтобы ознакомится с его командоми напиши'
                        '\n/help')

@dp.message_handler(commands=['help'])
async def process_help_cmd(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply(f'{user_full_name} - команды бота: \n\n /start - для запуска бота \n /help - для вывода данного поля помошника'
                        f'\n/ban - команда банит пользователя по выделенному сообщению'
                        f'\n/author - выводит информацию об авторе'
                        f'\n/rules - правила сервера'
                        f'\n\nА также в боте имеется фильтр нецензурной речи')

@dp.message_handler(commands=['author'])
async def author_cmd(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply('Автор - De_Sp1\n\nРазработан в целях обучения\nсоздания ботов')

@dp.message_handler(commands=['rules'])
async def author_cmd(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply('На данный момент особых правил нету,\nглавное не выражаться')