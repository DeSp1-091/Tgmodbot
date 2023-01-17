import time
import logging
from aiogram import types
from dispatcher import dp

mat = ["запрещенное слово", "запрешённая фраза", "запретка"]

@dp.message_handler()
async def filter_messages(message: types.Message):
    if any([i for i in mat if i in message.text]):
        user_id = message.from_user.id
        user_full_name = message.from_user.full_name
        logging.info(f'{user_id} {user_full_name} {time.asctime()}')
        await message.reply(f"Эй {user_full_name} слово, что ты написал находится в запрещённом списке слов\nЕсли продолжишь, то админ может тебя забанить")
        await message.delete()