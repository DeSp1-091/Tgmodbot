import time
import logging
from aiogram import types
import os
from dotenv import load_dotenv, find_dotenv
from dispatcher import dp


@dp.message_handler(is_admin=True, commands=["ban"])
async def cmd_ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение!")
        return
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')

    await message.bot.delete_message(message_id=message.message_id, chat_id=os.getenv('GROUP_ID'))
    await message.bot.kick_chat_member(chat_id=os.getenv('GROUP_ID'), user_id=message.reply_to_message.from_user.id)
    await message.reply_to_message.reply(f"Я ликвидировал эту цель!")


@dp.message_handler(content_types=["new_chat_members"])
async def on_user_joined(message: types.Message):
    await message.delete()

